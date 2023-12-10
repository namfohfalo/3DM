import _3dm_generator as generator
import algorytm_zachlanny as zachlanny
import potegowy3DM as potegowy

rozmiar_min = 2
rozmiar_max = 5
gestosc = 0.5
zbior_x = None
zbior_y = None
zbior_z = None
zbior_t = None

zbior_x, zbior_y, zbior_z, zbior_t = generator.generator(rozmiar_min, rozmiar_max, gestosc)

rozwiazanie_zachlanne = zachlanny.greedy_3dm(zbior_x, zbior_y, zbior_z, zbior_t)
rozwiazanie_potegowe = potegowy.power_set_3DM(zbior_t)

print(f"zachlanne: {rozwiazanie_zachlanne}")
print(f"potegowe: {rozwiazanie_potegowe}")