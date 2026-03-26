def intialise_variables():
    return {
        # Initial balance & Financials
        'initial_balance': 6_050_000,
        'interest_rate_annual': 0.10, # 10% per year compounded daily
        
        # Time variables
        'start_date': 730,
        'end_date': 1_460,
        
        # Production variables
        'initial_capacity': {
            'calopeia': 20,
            'sorange': 0,
            'tyran': 0,
            'entworpe': 0,
            'fardo': 0,
        },
        'factory_base_cost': 500_000,    # Flat cost for a new factory
        'capacity_upgrade_cost': 50_000, # Per drum/day capacity cost
        'capacity_upgrade_time': 90,
        
        'start_production_cost': 1_500,  # Base cost per batch
        'unit_cost': 1_000,              # Marginal cost per drum in batch
        
        # Warehousing & Inventory variables
        'warehouse_base_cost': 100_000,
        'warehouse_build_time': 60,
        'holding_cost_annual': 100,      # Per unit per year ($100/365 per day)
        
        # Sales variables
        'sale_price': 1_450,
        
        # Note: Delivery rules (truck limits, region costs) have been 
        # moved to helper.py to handle the complex continent/Fardo routing matrix.
        'truck_capacity': 200,
    }