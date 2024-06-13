def hvezdicky(zdroj="DATA/text.txt", cil="DATA/text2.txt"):
    with open(zdroj, 'r', encoding='utf-8') as z:
        radky = z.readlines()
        posledni = -1
        for i in radky:
            if "," not in radek:
                posledni = i

    if posledni != -1:
        radky.insert(posledni +1, "****************\n")
    else:
        radky.append("****************\n")


    with open(cil, "w", encoding="utf-8") as c:
        c.writelines(o_radky)

hvezdicky(zdroj="DATA/text.txt", cil="DATA/task4.txt")
print()