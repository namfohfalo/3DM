import random

def greedy_3dmrandom(T):
    solution = []  # List to store the selected triples
    best_solution_size = 0
    while T:
        # Choose random triple
        random.shuffle(T)

        # Select the triple
        selected_triple = T[0]

        # Add the selected triple to the solution
        solution.append(selected_triple)

        # Remove any triples that share elements with the selected triple
        T = [triple for triple in T if not any(element in selected_triple for element in triple)]
        
        current_solution_size = len(solution)
        if current_solution_size > best_solution_size:
            best_solution_size = current_solution_size

    return best_solution_size, solution