import random

def monte_carlo(N_pond, N_box, A_box):
    # Handle divide by zero case
    denominator = N_pond + N_box
    numerator = N_pond * A_box
    if denominator == 0:
        return 0
    
    return numerator / denominator

N = 1000
N_pond = 0
N_box = 0
A_box = 1
for i in range(N): 
    # Requirement no. 3
    # Requirement no. 4
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Requirement no. 5
    if x ** 2 + y ** 2 < 1:
        N_pond += 1
    else:
        N_box += 1
        
    # Requirement no. 6
    pi = monte_carlo(N_pond, N_box, A_box)
    
    if pi > 100:
        break

print('pi: {}'.format(pi))