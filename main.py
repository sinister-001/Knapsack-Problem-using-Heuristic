import random
import math

def knapsack_sa(weights, values, capacity, initial_temperature, cooling_rate, num_iterations):
    n = len(weights)
    current_solution = [random.randint(0, 1) for i in range(n)]
    current_value = sum([values[i] for i in range(n) if current_solution[i] == 1])
    current_weight = sum([weights[i] for i in range(n) if current_solution[i] == 1])
    best_solution = current_solution[:]
    best_value = current_value

    for i in range(num_iterations):
        temperature = initial_temperature / (1 + i)
        neighbor_solution = current_solution[:]
        j = random.randint(0, n-1)
        neighbor_solution[j] = 1 - neighbor_solution[j]
        neighbor_value = sum([values[i] for i in range(n) if neighbor_solution[i] == 1])
        neighbor_weight = sum([weights[i] for i in range(n) if neighbor_solution[i] == 1])

        if neighbor_weight <= capacity:
            if neighbor_value > current_value:
                current_solution = neighbor_solution[:]
                current_value = neighbor_value
                current_weight = neighbor_weight
                if current_value > best_value:
                    best_solution = current_solution[:]
                    best_value = current_value
            else:
                delta = neighbor_value - current_value
                probability = math.exp(delta/temperature)
                if random.random() < probability:
                    current_solution = neighbor_solution[:]
                    current_value = neighbor_value
                    current_weight = neighbor_weight

    return best_value, best_solution

# Define the problem instance
weights = [10, 300, 1, 200, 100]
values = [1000, 4000, 5000, 5000, 2000]
capacity = 400

# Set the parameters for the Simulated Annealing algorithm
initial_temperature = 10000
cooling_rate = 0.9999
num_iterations = 100000

# Run the Simulated Annealing algorithm
best_value, best_solution = knapsack_sa(weights, values, capacity, initial_temperature, cooling_rate, num_iterations)

# Print the results
print("Best value: ", best_value)
print("Best solution: ", best_solution)