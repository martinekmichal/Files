def Task1(soubor1, soubor2):
    with open(soubor1, "r", encoding="utf-8") as S1, open(soubor2, "r", encoding="utf-8") as S2:
        r1 = S1.readlines()
        r2 = S2.readlines()

    max_r = max(len(r1), len(r2))

    for i in range(max_r):
        if i < len(r1):
            l1 = r1[i].strip()
        else:
            print("bez řádku")
        if i < len(r2):
            l2 = r2[i].strip()
        else:
            print("bez řádku")

        if r1 != r2:
            print(f"Nesedí řádek {i+1}")
           # print(f"Soubor 1: {r1}")
           # print(f"Soubor 2: {r2}")

soubor1 = "DATA/L9T1_1.txt"
soubor2 = "DATA/L9T1_2.txt"

Task1(soubor1,soubor2)