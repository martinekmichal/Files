def kopiruj_radky(zdroj="DATA/text.txt", cil="DATA/text2.txt"):
    with open(zdroj, 'r', encoding='utf-8') as z:
        radky = z.readlines()
        o_radky = radky[::-1]

    with open(cil, "w", encoding="utf-8") as c:
        c.writelines(o_radky)

kopiruj_radky(zdroj="DATA/text.txt", cil="DATA/text3.txt")
print()

