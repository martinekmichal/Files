def task4_v2(input, output):
    with open(input, "r",  encoding='utf-8') as z:
        line = z.readlines()

        posledni = -1
        for i, line in enumerate(line):
            if "," not in line:
                posledni = i

        if posledni != -1:
            line.insert(posledni + 1, "***********\n")
        else:
            line.append()