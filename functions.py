import matplotlib.pyplot as plt
from variables import intialise_variables
from helper import divideRoundUp, get_transport_details, generateDemand

def startSimulation(events: list, plot=False):
    variables = intialise_variables()
    balance_history, inventory_history, production_history, stockouts = simulate(variables, events)
    
    if plot:
        plot_results(balance_history, inventory_history, production_history, stockouts, variables['start_date'])
        
    return balance_history, inventory_history, production_history, stockouts

def run_multiple_simulations(events: list, n: int = 100):
    """Runs the simulation n times and returns the average final balance."""
    final_balances = []
    for _ in range(n):
        # Run without plotting to save resources
        balance_history, _, _, _ = startSimulation(events, plot=False)
        final_balances.append(balance_history[-1])
    
    return sum(final_balances) / len(final_balances)

def simulate(variable: dict, events: list):
    start_date = variable['start_date']
    end_date = variable['end_date']

    balance_history = []
    inventory_history = []
    production_history = [] 
    
    events = sorted(events, key=lambda x: x['date'])
    regions = ['calopeia', 'sorange', 'tyran', 'entworpe', 'fardo']

    stockouts = []
    stockout_start = {region: None for region in regions}

    # Initialize Factories and Warehouses
    factory = {region: {
        'capacity': variable['initial_capacity'][region],
        'in_production': 0,
        'finished': 0,
        'pending_delivery_mode': None,
        'pending_delivery_region': None,
        'upgrade_schedule': []
    } for region in regions}

    inventory = {region: {
        'warehouse': 0,
        'transit': [], 
        'build_schedule': 0 
    } for region in regions}

    production_plan = {region: {} for region in regions}
    shipment_plan = {region: [] for region in regions}

    balance = variable['initial_balance']
    regions_with_warehouse = ['calopeia'] 
    regions_with_factories = ['calopeia'] 
    
    daily_holding_cost_rate = variable['holding_cost_annual'] / 365.0
    daily_interest_rate = variable['interest_rate_annual'] / 365.0

    for current_date in range(start_date, end_date):
        
        # 1. Financials: Accumulate Daily Interest
        if balance > 0:
            balance += balance * daily_interest_rate
            
        # 2. Process Timeline Events for today
        while len(events) > 0 and events[0]['date'] <= current_date:
            event = events.pop(0)
            action = event['action']
            
            if action == 'upgrade_capacity':
                fact_region = event['region']
                cap_upgrade = event['capacity']
                if cap_upgrade > 0:
                    if fact_region not in regions_with_factories:
                        balance -= variable['factory_base_cost']
                        regions_with_factories.append(fact_region)
                    
                    factory[fact_region]['upgrade_schedule'].append({
                        'capacity_upgrade': cap_upgrade, 
                        'days_to_upgrade': variable['capacity_upgrade_time']
                    })
                    balance -= cap_upgrade * variable['capacity_upgrade_cost']
                    
            elif action == 'set_reorder_policy':
                wh_region = event['warehouse']
                fact_region = event['factory']
                production_plan[wh_region][fact_region] = {
                    'order_quantity': event.get('qty', event.get('quantity')),
                    'reorder_point': event['rop'],
                    'delivery_mode': event.get('mode', 'truck'),
                    'priority': event.get('priority', 1) # Default to priority 1
                }
                
            elif action == 'set_fulfillment':
                wh_region = event['warehouse']
                if wh_region not in regions_with_warehouse:
                    balance -= variable['warehouse_base_cost']
                    inventory[wh_region]['build_schedule'] = variable['warehouse_build_time']
                    regions_with_warehouse.append(wh_region)
                
                shipment_plan[wh_region] = event['serves']

        # 3. Simulate Sales & Customer Fulfillment
        demands = generateDemand(current_date)
        for customer_region, demand in demands.items():
            if demand <= 0: continue
            
            candidate_warehouses = []
            for wh_region in regions_with_warehouse:
                if inventory[wh_region]['build_schedule'] > 0: continue
                if customer_region in shipment_plan[wh_region]:
                    mail_cost = get_transport_details(wh_region, customer_region, 'mail')['cost']
                    candidate_warehouses.append({
                        'region': wh_region,
                        'cost': mail_cost
                    })
            
            candidate_warehouses.sort(key=lambda x: x['cost'])

            for candidate in candidate_warehouses:
                wh_region = candidate['region']
                mail_cost = candidate['cost']
                
                fulfilled = min(demand, inventory[wh_region]['warehouse'])
                if fulfilled > 0:
                    inventory[wh_region]['warehouse'] -= fulfilled
                    demand -= fulfilled
                    balance += fulfilled * variable['sale_price']
                    balance -= fulfilled * mail_cost
                
                if demand <= 0: break
        
        # 4. Manage Warehouses & Transit
        for wh_region in regions_with_warehouse:
            if inventory[wh_region]['build_schedule'] > 0:
                inventory[wh_region]['build_schedule'] -= 1
                continue

            for transit in inventory[wh_region]['transit'][:]:
                transit['days_to_arrival'] -= 1
                if transit['days_to_arrival'] <= 0:
                    inventory[wh_region]['warehouse'] += transit['quantity']
                    inventory[wh_region]['transit'].remove(transit)

        # 5. Manage Factories & Production (Implementing the 4 Criteria)
        for fact_region in regions_with_factories:
            
            # Upgrade completion
            if len(factory[fact_region]['upgrade_schedule']) > 0:
                if factory[fact_region]['upgrade_schedule'][0]['days_to_upgrade'] > 0:
                    factory[fact_region]['upgrade_schedule'][0]['days_to_upgrade'] -= 1
                else:
                    factory[fact_region]['capacity'] += factory[fact_region]['upgrade_schedule'][0]['capacity_upgrade']
                    factory[fact_region]['upgrade_schedule'].pop(0)

            # CRITERIA 4: Is the factory idle? (And does it have capacity to actually work?)
            if factory[fact_region]['in_production'] == 0 and factory[fact_region]['finished'] == 0 and factory[fact_region]['capacity'] > 0:
                
                candidate_orders = []
                
                # Scan all warehouses to see if they trigger production
                for wh_region in regions_with_warehouse:
                    if inventory[wh_region]['build_schedule'] > 0: continue
                    
                    plan = production_plan[wh_region].get(fact_region)
                    if not plan: continue
                    
                    qty = plan['order_quantity']
                    rop = plan['reorder_point']
                    mode = plan['delivery_mode']
                    priority = plan['priority']
                    
                    # CRITERIA 2: order quantity > 0
                    if qty <= 0: continue
                    
                    # CRITERIA 1: Inventory + Transit <= ROP
                    total_inventory = inventory[wh_region]['warehouse'] + sum(t['quantity'] for t in inventory[wh_region]['transit'])
                    if total_inventory > rop: continue
                    
                    # CRITERIA 3: Sufficient cash to pay for production AND shipping
                    transport = get_transport_details(fact_region, wh_region, mode)
                    if mode == 'truck':
                        shipping_cost = divideRoundUp(qty, variable['truck_capacity']) * transport['cost']
                    else:
                        shipping_cost = qty * transport['cost']
                        
                    total_cost = variable['start_production_cost'] + (qty * variable['unit_cost']) + shipping_cost
                    
                    if balance >= total_cost:
                        candidate_orders.append({
                            'wh_region': wh_region,
                            'priority': priority,
                            'qty': qty,
                            'mode': mode,
                            'total_cost': total_cost
                        })
                
                # If multiple warehouses triggered, prioritize them!
                if candidate_orders:
                    # Sort by priority integer descending (e.g., Priority 2 evaluated before Priority 1)
                    candidate_orders.sort(key=lambda x: x['priority'], reverse=True)
                    best_order = candidate_orders[0]
                    
                    # Deduct full cost upfront
                    balance -= best_order['total_cost']
                    
                    # Lock the factory into production
                    factory[fact_region]['in_production'] = best_order['qty']
                    factory[fact_region]['pending_delivery_mode'] = best_order['mode']
                    factory[fact_region]['pending_delivery_region'] = best_order['wh_region']

            # Daily production progress
            if factory[fact_region]['in_production'] > 0:
                production_amount = min(factory[fact_region]['in_production'], factory[fact_region]['capacity'])
                factory[fact_region]['in_production'] -= production_amount
                factory[fact_region]['finished'] += production_amount

            # Shipping finished batch
            # Checked immediately after production so the factory becomes "idle" tomorrow
            if factory[fact_region]['in_production'] == 0 and factory[fact_region]['finished'] > 0:
                dest_region = factory[fact_region]['pending_delivery_region']
                mode = factory[fact_region]['pending_delivery_mode']
                
                # Cost was paid upfront, just get the delivery time
                transport = get_transport_details(fact_region, dest_region, mode)
                
                inventory[dest_region]['transit'].append({
                    'quantity': factory[fact_region]['finished'],
                    'days_to_arrival': transport['time']
                })
                
                # Clear factory to idle
                factory[fact_region]['finished'] = 0
                factory[fact_region]['pending_delivery_region'] = None
                factory[fact_region]['pending_delivery_mode'] = None

        # 6. Apply Holding Costs
        total_finished_drums = 0
        for r in regions:
            total_finished_drums += inventory[r]['warehouse']
            total_finished_drums += sum(t['quantity'] for t in inventory[r]['transit'])
        balance -= total_finished_drums * daily_holding_cost_rate
    
        # Track stockouts (contiguous periods where inventory is zero)
        for region in regions:
            # Only track for active warehouses that have finished building
            if region in regions_with_warehouse and inventory[region]['build_schedule'] == 0:
                if inventory[region]['warehouse'] == 0:
                    if stockout_start[region] is None:
                        stockout_start[region] = current_date
                else:
                    if stockout_start[region] is not None:
                        stockouts.append({
                            'region': region,
                            'start_date': stockout_start[region],
                            'end_date': current_date - 1
                        })
                        stockout_start[region] = None

        balance_history.append(balance)
        production_history.append({r: factory[r]['in_production'] + factory[r]['finished'] for r in regions})
        inv_copy = {k: {'warehouse': v['warehouse'], 'transit': list(v['transit'])} for k, v in inventory.items()}
        inventory_history.append(inv_copy)

    # Close any open stockout periods at the end of the simulation
    for region, s_date in stockout_start.items():
        if s_date is not None:
            stockouts.append({
                'region': region,
                'start_date': s_date,
                'end_date': end_date - 1
            })

    return balance_history, inventory_history, production_history, stockouts

def plot_results(balance_history, inventory_history, production_history, stockouts, start_date):
    days = list(range(start_date, start_date + len(balance_history)))
    
    # Increased figure height to fit 4 subplots cleanly
    plt.figure(figsize=(14, 16)) 
    
    # 1. Cash Balance Plot
    plt.subplot(4, 1, 1)
    plt.plot(days, balance_history, label="Cash Balance", color='green', linewidth=2)
    plt.title("Supply Chain Simulation Results")
    plt.ylabel("Balance ($)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # 2. Inventory Plot
    plt.subplot(4, 1, 2)
    regions = inventory_history[0].keys()
    for region in regions:
        region_inventory = [day_data[region]['warehouse'] for day_data in inventory_history]
        if any(inv > 0 for inv in region_inventory):
            plt.plot(days, region_inventory, label=f"{region.capitalize()} Warehouse Inventory", linewidth=1.5)
            
    plt.ylabel("Inventory Level (Drums)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # 3. Production Plot
    plt.subplot(4, 1, 3)
    prod_regions = production_history[0].keys()
    for region in prod_regions:
        region_prod = [day_data[region] for day_data in production_history]
        if any(p > 0 for p in region_prod):
            plt.plot(days, region_prod, label=f"{region.capitalize()} Production", linewidth=1.5)
            
    plt.ylabel("Units in Production (Drums)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 4. Stockout Plot (NEW)
    plt.subplot(4, 1, 4)
    all_regions = list(inventory_history[0].keys())
    for i, region in enumerate(all_regions):
        region_stockouts = [s for s in stockouts if s['region'] == region]
        # Format for broken_barh: [(start, duration), ...]
        xranges = [(s['start_date'], s['end_date'] - s['start_date'] + 1) for s in region_stockouts]
        if xranges:
            plt.broken_barh(xranges, (i - 0.4, 0.8), label=f"{region.capitalize()} Stockout", 
                            facecolors=plt.cm.tab10(i % 10))
            
    plt.yticks(range(len(all_regions)), [r.capitalize() for r in all_regions])
    plt.xlabel("Day")
    plt.ylabel("Stockout Periods by Regions")
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()