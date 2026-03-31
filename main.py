from functions import startSimulation, run_multiple_simulations


updated_events = [
    ### Keep at Calopeia ###
    # --- DAY 730: Stage 1 ---
    {
        'date': 730, 'action': 'upgrade_capacity', 
        'region': 'calopeia', 'capacity': 80
    },
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'calopeia', 'serves': ['calopeia', 'tyran']
    },

    ### MISTAKE 1 ACCIDENTALLY PLACED AN ORDER OF 1000 FOR CALOPEIA WH ###
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 1000, 'rop': 200, 'mode': 'truck', 'priority': 3
    },
    {
        'date': 731, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 3
    },
    {
        'date': 820, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 400, 'rop': 1000, 'mode': 'truck', 'priority': 3
    },

    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 400, 'rop': 1000, 'mode': 'truck', 'priority': 1
    },

    {
        'date': 1180, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 600, 'rop': 1000, 'mode': 'truck', 'priority': 3
    },

    ## Send to Sorange ###
    {
        'date': 755, 'action': 'set_fulfillment', 
        'warehouse': 'sorange', 'serves': ['sorange']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 2
    },
    {
        'date': 820, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 400, 'rop': 1000, 'mode': 'truck', 'priority': 2
    },

    ## Send to tyran ###

    ### Mistake 2 ACCIDENTALLY BUILT WAREHOUSE IN TYRAN ###
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'tyran', 'serves': ['tyran']
    },
    {
        'date': 760, 'action': 'set_reorder_policy', 
        'warehouse': 'tyran', 'factory': 'calopeia', 
        'qty': 200, 'rop': 100, 'mode': 'truck', 'priority': 4
    },

    # --- End Production ---
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 0
    },
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'tyran', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 0
    },
    {
        'date': 1430, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 0
    },
    
]

if __name__ == "__main__":
    iterations = 100

    startSimulation(updated_events, plot=True, use_excel_demand=True)

    print(f"\nRunning Monte Carlo Simulation (N={iterations}) for Static ROP No Entworpe Plan...")
    final_balance = run_multiple_simulations(updated_events, n=iterations)
    print(f"Average Balance over {iterations} runs: ${sum(final_balance)/len(final_balance):,.2f}")
    print(f"Minimum Balance over {iterations} runs: ${min(final_balance):,.2f}")
    print(f"Maximum Balance over {iterations} runs: ${max(final_balance):,.2f}")
