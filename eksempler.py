antal_aar = 5
aar = 0
hovedstol = 143000
gaeld = hovedstol
rente = 0.03
for arr in range(antal_aar):
    gaeld *= 1 + rente

print(gaeld)


if gaeld > hovedstol * antal_aar * rente:
    print("Renters rente!")
elif gaeld < hovedstol * antal_aar * rente:
    print("Underligt...")
else:
    print("Heller ikke normalt")