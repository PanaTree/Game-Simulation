from functions import startSimulation, run_multiple_simulations

timeline_events = [
       

    ### Calopeia ###

     # --- DAY 730: Q1 Initial Setup ---
    {
        'date': 730, 'action': 'upgrade_capacity', 
        'region': 'calopeia', 'capacity': 40
    },
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'calopeia', 'serves': ['calopeia']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 407, 'mode': 'truck', 'priority': 2
    },

    # --- DAY 820: Q2 ---
    {
        'date': 820, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 600, 'rop': 1052, 'mode': 'truck', 'priority': 2
    },

    # --- DAY 910: Q3 ---
    {
        'date': 910, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 600, 'rop': 1120, 'mode': 'truck', 'priority': 2
    },
    # --- DAY 1000: Q4 ---
    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 400, 'rop': 310, 'mode': 'truck', 'priority': 2
    },
    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 400, 'rop': 200, 'mode': 'truck', 'priority': 1
    },

    # --- DAY 1090: Q5 ---
    {
        'date': 1090, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 400, 'rop': 340, 'mode': 'truck', 'priority': 2
    },

    # --- DAY 1120: 60 Days Before Q6 ---
    {
        'date': 1120, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 600, 'rop': 1052, 'mode': 'truck', 'priority': 2
    },

    # --- DAY 1270: Q7 ---
    {
        'date': 1270, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 600, 'rop': 1120, 'mode': 'truck', 'priority': 2
    },

    # --- DAY 1360: Q8 ---
    {
        'date': 1360, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 200, 'rop': 200, 'mode': 'truck', 'priority': 2
    },

    # --- DAY 1400: End Production ---
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 2
    },
    {
        'date': 1400, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 1
    },


    ### Sorange ###
     # --- DAY 730: Q1 Initial Setup ---
    {
        'date': 730, 'action': 'upgrade_capacity', 
        'region': 'sorange', 'capacity': 40
    },
    {
        'date': 730, 'action': 'set_fulfillment', 
        'warehouse': 'sorange', 'serves': ['sorange']
    },
    {
        'date': 730, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'sorange', 
        'qty': 200, 'rop': 1000, 'mode': 'truck', 'priority': 2
    },
    # --- DAY 1430: End Production ---
    {
        'date': 1430, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'sorange', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 2
    },
]

if __name__ == "__main__":
    # print("Running Single Simulation with Plots...")
    # balance, inventory, production, stockouts = startSimulation(timeline_events, plot=True)

    # print("\n--- Single Run Results ---")
    # print(f"Final Cash Balance: ${balance[-1]:,.2f}")

    print("\nRunning Monte Carlo Simulation (N=100)...")
    iterations = 100
    avg_balance = run_multiple_simulations(timeline_events, n=iterations)
    print(f"Average Final Balance over {iterations} runs: ${avg_balance:,.2f}")
