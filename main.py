from functions import startSimulation

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
    {
        'date': 820, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 200, 'rop': 400, 'mode': 'truck', 'priority': 1
    },
    # --- DAY 1000: Q4 ---
    {
        'date': 1000, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 400, 'rop': 310, 'mode': 'truck', 'priority': 2
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

    # --- DAY 1360: End Production ---
    {
        'date': 1360, 'action': 'set_reorder_policy', 
        'warehouse': 'calopeia', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 2
    },
    {
        'date': 1360, 'action': 'set_reorder_policy', 
        'warehouse': 'sorange', 'factory': 'calopeia', 
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 1
    },


    ### Sorange ###
     # --- DAY 730: Q1 Initial Setup ---
    {
        'date': 730, 'action': 'upgrade_capacity', 
        'region': 'sorange', 'capacity': 50
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
        'qty': 0, 'rop': 0, 'mode': 'truck', 'priority': 1
    },
]

print("Running Supply Chain Game Simulation...")
# Added sales to the returned variables!
balance, inventory, sales = startSimulation(timeline_events, plot=True)

print("\n--- Simulation Complete ---")
print(f"Final Cash Balance (Day 1460): ${balance[-1]:,.2f}")
print(f"Final Inventory in Calopeia: {inventory[-1]['calopeia']['warehouse']} drums")


