def Task3(zdroj="DATA/text.txt", cil="DATA/L9T3_1.txt"):
    with open(zdroj, 'r', encoding='utf-8') as z:
        radky = z.readlines()
        radky = radky[:-1]

    with open(cil, "w", encoding="utf-8") as c:
        c.writelines(radky)

Task3(zdroj="DATA/text.txt", cil="DATA/L9T3_1.txt")
print()