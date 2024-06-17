def Task2(slovo: object) -> object:
    samohlaska = 0
    souhlaska = 0

    for p in slovo:
        if p.isalpha():
            if p.lower() in "aeiou" and p.lower() in "áéíóů":
                samohlaska += 1
            else:
                souhlaska += 1
    return samohlaska, souhlaska

def soucty_hodnot(slovo):
    return sum(p.isdigit() for p in slovo)

zdroj = "DATA/L9T1_1.txt"
cil = "DATA/L9T2.txt"

p_znak = 0
p_radek = 0
p_souhlaska = 0
p_samohlaska = 0
p_celkem = 0

with open(zdroj,"r", encoding="utf-8") as S1:
    for r in S1:
        p_znak += len(r)
        p_radek += 1
        slovoo = r.split()

        for s in slovoo:
           samohlaska, souhlaska = Task2(slovoo)
           p_samohlaska += samohlaska
           p_souhlaska += souhlaska
           p_celkem += soucty_hodnot(slovoo)

with open(cil, "w", encoding="UTF-8") as S2:
    S2.write(f"Znaků: {p_znak}\n")
    S2.write(f"Řádků: {p_radek}\n")
    S2.write(f"Samohlásek: {p_samohlaska}\n")
    S2.write(f"Souhlásek: {p_souhlaska}\n")
    S2.write(f"Dohromady: {p_celkem}\n")

print("Bylo zapsáno do souboru 'cil=DATA/L9T2.txt' " )

# zde jsme se zasekl kvůli kopirovaní řádku.... řádek 25 jsme překopíroval na řádek 37 ..... zásek byl na ve znaménku "w"
