def Task4(zdroj="DATA/L9T2.txt", cil="DATA/L9T4_1.txt"):
    with open(zdroj, 'r', encoding='utf-8') as z:
        radky = z.readlines()
        max_radek = max(len(radek) for radek in radky)

    with open(cil, "w", encoding="utf-8") as c:
        c.write(f"Nejdelší řádek je: {max_radek}")
        #print(max_radek)

Task4(zdroj="DATA/L9T2.txt", cil="DATA/L9T4_1.txt")
