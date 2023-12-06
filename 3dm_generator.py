import random

def generator(min_array_size, max_array_size, density): #Dla density = 0.5 stworzy około 40% z możliwych do utworzenia trójek ze względu na duplikaty
    X = [i for i in range(random.randint(min_array_size, max_array_size))]
    Y = [i for i in range(random.randint(min_array_size, max_array_size))]
    Z = [i for i in range(random.randint(min_array_size, max_array_size))]
    triplets = []
    for _ in range(round(len(X)*len(Y)*len(Z)*density)):
        a = random.randint(0, len(X) - 1)
        b = random.randint(0, len(Y) - 1)
        c = random.randint(0, len(Z) - 1)
        if [a, b, c] not in triplets:
            triplets.append([a, b, c])
    return X, Y, Z, triplets

print(generator(2, 5, 0.5))