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
"""
vek = int(input("Kolik ti je let?"))
obcan = input("Jseš občanem ČR?")

if vek >= 18 and obcan == "ano":
    print("Můžeš volit!")
else:
    print("Nemůžeš volit!")
"""
"""
if vek >= 18:
    if obcan == "ano":
        print("Můžeš volit!")
    else:
        print("Nemůžeš volit!")
else:
    print("Nemůžeš volit!")
"""
"""
for _ in range(100):
    print("Ahoj")
"""






"""
text = input("Zadej text: ")
print(f"Velkými písmeny: {text.upper()}")
print(f"Malými písmeny: {text.lower()}")
print(f"Počet znak: {len(text)}")
print(f"První znak: {text[0]}")
print(f"Poslední znak: {text[-1]}")
print(f"Text pozpátku: {text[::-1]}")
"""
"""
seznam = ["Matrix", "Logan"]
for _ in range(3):
    film = input("Zadej název filmu: ")
    seznam.append(film)
print("Tvoje oblíbené filmy jsou:")
for film in seznam:
    print(film)
print(f"V seznamu je: {len(seznam)} filmů")
"""