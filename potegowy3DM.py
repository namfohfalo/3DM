import itertools
import random

# Do testowania
# def generator(min_array_size, max_array_size, density): #Dla density = 0.5 stworzy około 40% z możliwych do utworzenia trójek ze względu na duplikaty
#     X = [i for i in range(random.randint(min_array_size, max_array_size))]
#     Y = [i for i in range(random.randint(min_array_size, max_array_size))]
#     Z = [i for i in range(random.randint(min_array_size, max_array_size))]
#     triplets = []
#     for _ in range(round(len(X)*len(Y)*len(Z)*density)):
#         a = random.randint(0, len(X) - 1)
#         b = random.randint(0, len(Y) - 1)
#         c = random.randint(0, len(Z) - 1)
#         if [a, b, c] not in triplets:
#             triplets.append([a, b, c])
#     return X, Y, Z, triplets

# Zmieniony generator zbioru potęgowego aby tworzył od zbioru rozwiązań o największej długości
def genzbiorpotegowy(zbior):
  n = len(zbior)
  for i in range( n,-1,  -1):
   for c in itertools.combinations(zbior,i):
     yield(list(c))

# Sprawdzenie poprawności wyniku
def check_solution(solutions):
  used = [set({}),set({}),set({})]
  for solution in solutions:
    for i in range(3):
      if(solution[i] in used[i]):
        return False
      else:
        used[i].add(solution[i])
  return True

def power_set_3DM(zbior):
  best_sol = 0
  solution = []
  for c in genzbiorpotegowy(zbior):
   if(check_solution(c)):
     best_sol = len(c)
     solution = c
     return best_sol, solution

#Przykład
# t = generator(3,4,0.5)
# zbior = t[3]
# print("Solution: ", power_set_3DM(zbior))