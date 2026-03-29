from functions import startSimulation, run_multiple_simulations

cluade_events = [
    ### Claude Plan ###
    ### Keep at Calopeia ###
    # --- DAY 730: Stage 1 ---
    {
        'date': 730, 'action': 'upgrade_capacity', 
        'region': 'calopeia', 'capacity': 80
    },
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'calopeia', 'serves': ['calopeia', 'tyran', 'entworpe']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 3
    },

    ## Send to Sorange ###
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'sorange', 'serves': ['sorange']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 200, 'rop': 800, 'mode': 'truck', 'priority': 3
    },

    # --- End Production ---
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 3
    },
    {
        'date': 1430, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 3
    },
]

no_entworpe_events = [
    ### Claude Plan ###
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
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 4
    },

    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 2
    },

    {
        'date': 1180, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 4
    },

    ## Send to Sorange ###
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'sorange', 'serves': ['sorange']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 3
    },

    # --- End Production ---
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 3
    },
    {
        'date': 1430, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 3
    },
]

dynamic_events = [

    ### Main Plan (Modifed From Claude) ###

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
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 865, 'mode': 'truck', 'priority': 3
    },
    # --- DAY 1000: Stage 2 ---
    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 455, 'mode': 'truck', 'priority': 3
    },
    # --- DAY 1180: Stage 3 ---
    {
        'date': 1180, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 865, 'mode': 'truck', 'priority': 3
    },
    # --- DAY 1360: Stage 4 ---
    {
        'date': 1360, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 560, 'mode': 'truck', 'priority': 3
    },



    ## Send to Sorange ###
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'sorange', 'serves': ['sorange']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 200, 'rop': 800, 'mode': 'truck', 'priority': 3
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 865, 'mode': 'truck', 'priority': 3
    },
    # --- DAY 1000: Stage 2 ---
    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 455, 'mode': 'truck', 'priority': 3
    },
    # --- DAY 1180: Stage 3 ---
    {
        'date': 1180, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 865, 'mode': 'truck', 'priority': 3
    },
    # --- DAY 1360: Stage 4 ---
    {
        'date': 1360, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 560, 'mode': 'truck', 'priority': 3
    },

    # --- End Production ---
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 3
    },
    {
        'date': 1430, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 3
    },
]

if __name__ == "__main__":
    iterations = 100

    print(f"\nRunning Monte Carlo Simulation (N={iterations}) for Claude's Static ROP Plan...")
    final_balance = run_multiple_simulations(cluade_events, n=iterations)
    print(f"Average Balance over {iterations} runs: ${sum(final_balance)/len(final_balance):,.2f}")
    print(f"Minimum Balance over {iterations} runs: ${min(final_balance):,.2f}")
    print(f"Maximum Balance over {iterations} runs: ${max(final_balance):,.2f}")

    print(f"\nRunning Monte Carlo Simulation (N={iterations}) for Static ROP No Entworpe Plan...")
    final_balance = run_multiple_simulations(no_entworpe_events, n=iterations)
    print(f"Average Balance over {iterations} runs: ${sum(final_balance)/len(final_balance):,.2f}")
    print(f"Minimum Balance over {iterations} runs: ${min(final_balance):,.2f}")
    print(f"Maximum Balance over {iterations} runs: ${max(final_balance):,.2f}")

    print(f"\nRunning Monte Carlo Simulation (N={iterations}) for Team's Dynamic ROP Plan...")
    final_balance = run_multiple_simulations(dynamic_events, n=iterations)
    print(f"Average Balance over {iterations} runs: ${sum(final_balance)/len(final_balance):,.2f}")
    print(f"Minimum Balance over {iterations} runs: ${min(final_balance):,.2f}")
    print(f"Maximum Balance over {iterations} runs: ${max(final_balance):,.2f}")