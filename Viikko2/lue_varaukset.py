from datetime import datetime

def main():
    varaukset = "varaukset.txt"

    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    varaus = varaus.split("|")

    paiva = datetime.strptime(varaus[2], "%Y-%m-%d")
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus[3], "%H:%M")
    suomalainenAika = aika.strftime("%H.%M")

    varausnumero = int(varaus[0])
    varaaja = str(varaus[1])
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d")
    aika = datetime.strptime(varaus[3], "%H:%M")
    tuntimäärä = int(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = tuntimäärä * tuntihinta
    maksettu = varaus[6].strip() == "True"
    kohde = str(varaus[7])
    puhelin = str(varaus[8])
    sähköposti = str(varaus[9])

    print()
    print(f"Varausnumero: {varausnumero}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {suomalainenPaiva}")
    print(f"Aloitusaika: {suomalainenAika}")
    print(f"Tuntimäärä: {tuntimäärä}")
    print(f"Tuntihinta: {tuntihinta:.2f} €")
    print(f"Kokonaishinta: {kokonaishinta:.2f} €")
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {sähköposti}")

if __name__ == "__main__":
    main()