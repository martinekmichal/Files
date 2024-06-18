def Task6(zdroj="DATA/text.txt", h_slovo="", n_slovo=""):
    with open(zdroj, 'r', encoding='utf-8') as z:
        obsah = z.read()
        h_slovo = input("Zadej slovo které bude nahrazeno: ")
        n_slovo = input("Zadej slovo kterým chces hledané změnit: ")
        n_obsah = obsah.replace(h_slovo, n_slovo)

    with open(zdroj, 'w', encoding='utf-8') as c:
        c.write(n_obsah)
        print(f"Slovo {h_slovo} jsi nahradil slovem {n_slovo}.")

Task6()


