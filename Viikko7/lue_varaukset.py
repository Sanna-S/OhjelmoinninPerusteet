# Copyright (c) 2025 Sanna Sjöblad
# Licence: MIT


from datetime import datetime

def muunna_varaustiedot(varaus_lista: list[str]) -> dict:
    return {
        "Id": int(varaus_lista[0]),
        "Nimi": varaus_lista[1],
        "Sahköposti": varaus_lista[2],
        "Puhelin": varaus_lista[3],
        "Paiva": datetime.strptime(varaus_lista[4], "%Y-%m-%d").date(),
        "Kellonaika": datetime.strptime(varaus_lista[5], "%H:%M").time(),
        "Kesto": int(varaus_lista[6]),
        "Hinta": float(varaus_lista[7]),
        "Vahvistettu": varaus_lista[8].lower() == "true",
        "Tila": varaus_lista[9],
        "Luotu": datetime.strptime(varaus_lista[10], "%Y-%m-%d %H:%M:%S")
    }

def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus['Vahvistettu']):
            print(f"- {varaus['Nimi']}, {varaus['Tila']}, {varaus['Paiva'].strftime('%d.%m.%Y')} klo {varaus['Kellonaika'].strftime('%H.%M')}")

    print()

def pitkat_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus['Kesto'] >= 3):
            print(f"- {varaus['Nimi']}, {varaus['Paiva'].strftime('%d.%m.%Y')} klo {varaus['Kellonaika'].strftime('%H.%M')}, kesto {varaus['Kesto']} h, {varaus['Tila']}")

    print()

def varausten_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus['Vahvistettu']):
            print(f"{varaus['Nimi']} → Vahvistettu")
        else:
            print(f"{varaus['Nimi']} → EI vahvistettu")

    print()

def varausten_lkm(varaukset: list):
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0
    for varaus in varaukset[1:]:
        if(varaus['Vahvistettu']):
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl")
    print()

def varausten_kokonaistulot(varaukset: list):
    varaustenTulot = 0
    for varaus in varaukset[1:]:
        if(varaus['Vahvistettu']):
            varaustenTulot += varaus['Kesto']*varaus['Hinta']

    print("Vahvistettujen varausten kokonaistulot:", f"{varaustenTulot:.2f}".replace('.', ','), "€")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()