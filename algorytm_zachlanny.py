def greedy_3dm(X, Y, Z, T):
    solution = []  # List to store the selected triples

    while T:
        # Sort triples by size in ascending order
        sorted_triples = sorted(T, key=lambda triple: len(set(triple)))

        # Select the triple with the fewest elements
        selected_triple = sorted_triples[0]

        # Add the selected triple to the solution
        solution.append(selected_triple)

        # Remove any triples that share elements with the selected triple
        T = [triple for triple in T if not any(element in selected_triple for element in triple)]

    return solution

# Example usage:
X = {1, 2, 3}
Y = {4, 5, 6}
Z = {7, 8, 9}
T = [{1, 4, 7}, {2, 5, 8}, {2, 6, 9}, {3, 6, 9}, {1, 5, 9}, {2, 6, 7}]

solution = greedy_3dm(X, Y, Z, T)
print("Selected triples:", solution)
