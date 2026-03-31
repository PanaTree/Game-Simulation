import math
import random

def divideRoundUp(a, b):
    result = a // b
    if a % b > 0: 
        result += 1
    return result

def get_transport_details(origin, dest, mode):
    """
    Returns a dictionary with 'cost' and 'time' based on the game's region rules.
    """
    # Same region
    if origin == dest:
        if mode == 'truck': return {'cost': 15000, 'time': 7}
        else: return {'cost': 150, 'time': 1}
        
    # Between continent and Fardo
    elif origin == 'fardo' or dest == 'fardo':
        if mode == 'truck': return {'cost': 45000, 'time': 14}
        else: return {'cost': 400, 'time': 2}
        
    # Different regions on the continent
    else:
        if mode == 'truck': return {'cost': 20000, 'time': 7}
        else: return {'cost': 200, 'time': 1}

def generateDemand(current_date: int):
    """
    Simulates demand based on the rules in the PDF manual and empirical CSV/Image data.
    """
    # End of Life multiplier: Decreases linearly from 1430 to 1460
    eol_multiplier = 1.0
    if current_date >= 1430:
        eol_multiplier = max(0.0, (1460 - current_date) / 30.0)

    # 1. Calopeia: Smooth trigonometric seasonal curve
    calopeia_mean = 39.19 - 30.89 * math.cos(2 * math.pi * current_date / 365)
    
    # Variance dynamically scales with the mean. 
    calopeia_demand = max(0, int(random.gauss(calopeia_mean, calopeia_mean*0.2)))

    # Regions outside Calopeia ONLY begin tracking/ordering on Day 640
    if current_date < 640:
        sorange_demand = 0
        tyran_demand = 0
        entworpe_demand = 0
        fardo_demand = 0
    else:

        # 2. Sorange: EXPLOSIVE Linear growth confirmed by Day 730 graph.
        sorange_mean = max(0, 0.15*current_date - 97.45)
        sorange_demand = max(0, int(random.gauss(sorange_mean, sorange_mean * 0.2)))

        # 3. Tyran:
        tyran_demand = max(0, int(random.gauss(16.78, 16.22)))

        # 4. Fardo: Highly variable.
        fardo_demand = max(0, int(random.gauss(15.7, 16.77)))

        # 5. Entworpe: Reorder point of 250 units. 
        entworpe_prob = 0.044
        entworpe_demand = 250 if random.random() < entworpe_prob else 0

    return {
        'calopeia': int(calopeia_demand * eol_multiplier),
        'sorange': int(sorange_demand * eol_multiplier),
        'tyran': int(tyran_demand * eol_multiplier),
        'entworpe': int(entworpe_demand * eol_multiplier),
        'fardo': int(fardo_demand * eol_multiplier),
    }