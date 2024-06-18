def Task5(zdroj="DATA/text.txt", cil="DATA/L9T5.txt"):
    slovo = input("Zadej slovo které chceš hledat kolikrát je v textu: ")
    pocet = 0
    with open(zdroj, 'r', encoding='utf-8') as z:
        for radek in z:
            pocet += radek.count(slovo)

    with open(cil, "w", encoding="utf-8") as c:
        c.write(f"Slovo {slovo} se v textu vyskytuje {pocet} krát.")

Task5(zdroj="DATA/text.txt", cil="DATA/L9T5.txt")
