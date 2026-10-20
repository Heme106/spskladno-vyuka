# Ukázka funkce input()
"""
print("Jak se jmenujes?")
input()
jmeno = input("Jak se jmenuješ? ")
jidlo = input("Jaké je tvé oblíbené jídlo? ")

print()
print("Ahoj,", jmeno + "!")
print("Tvé oblíbené jídlo je:", jidlo
"""
"""
prvni = input("Zadej první číslo")
druhy = input("Zadej druhé číslo")
prvni = float(prvni)
druhy = float(druhy)
print("součet:", prvni+druhy)
print("rozdíl:", prvni-druhy)
print("součin:", prvni*druhy)
"""

vek = int(input("Kolik ti je let?"))
obcan = input("Jseš občanem ČR?")

if vek >= 18 and obcan == "ano":
    print("Můžeš volit!")
else:
    print("Nemůžeš volit!")

"""
if vek >= 18:
    if obcan == "ano":
        print("Můžeš volit!")
    else:
        print("Nemůžeš volit!")
else:
    print("Nemůžeš volit!")
"""