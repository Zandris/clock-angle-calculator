def f(ora, perc):
    ora_szog = (ora % 12) * 30 + perc * 0.5

    perc_szog = perc * 6

    szog = abs(ora_szog - perc_szog)

    szog = min(szog, 360 - szog)

    return szog

ora = input("óra: ")
perc = input("perc: ")
szog = f(int(ora), int(perc))
print(szog)

