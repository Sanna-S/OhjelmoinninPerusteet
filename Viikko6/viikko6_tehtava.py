# Copyright (c) 2025 Sanna Sjöblad
# Licence: MIT

from datetime import datetime, date, timedelta

def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa jokaisen annetun tietorivin tietotyypit oikeiksi.
    
    Parametrit:
    tietue: sisältää neljä kenttää merkkijonoina: joista ensimmäinen date (muotoa 'pp.kk.vvvv') ja loput float.

    Palauttaa:
    listan, jossa muutetut tietotyypit
    """
    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", "."))
    ]
    
def lue_date(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit oikeassa rakenteessa ja tietotyypeissä.
    Kutsuu apufunktiota muunna_tiedot muuttaakseen tietotyypit.
     funktio palauttaa listan, jolloin tietotyypit on muutettu oikeiksi.

    Parametrit:
    tiedoston_nimi (str): ottaa vastaan tiedoston jossa kentät eroteltu puolipisteillä.

    Palauttaa:
    tietokanta (list): palauttaa tietokannan, jossa tietotyypit on muutettu.   
    """
    
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # ohitetaan kenttien esittelytiedot
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta

def raportti_tiedostoon(raportti: str):
    """
    Kirjoittaa raportin tiedostoon raportti.txt.
    Parametrit:
    raportti (str): raporttiteksti
"""
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)


def muotoile_raportti(otsikko: str, kulutus: float, tuotanto: float, lampotila: float, tietue_lkm: int) -> str:
    """"
    Muotoilee raportin annetulla otsikolla ja arvoilla.
    """
    raportti = "-" * 50 + "\n"
    raportti += f"{otsikko}\n"
    raportti += f"-Kokonaiskulutus: " + f"{kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"-Kokonaistuotanto: " + f"{tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"-Keskilämpötila: " + f"{lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "-" * 50 + "\n"
    return raportti

def raportti_aikavali(alkupaiva: str, loppupaiva: str, tietokanta: list) -> str:
    """
    Raportiin tulostetaan aikaväliltä:
    - Alkupäivämäärä ja loppupäivämäärä (pp.kk.vvvv-pp.kk.vvvv)
    - Aikavälin kokonaiskulutuksen (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Aikavälin kokonaistuotannon (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Aikavälin keskilämpötila (°C, esim. kaikkien tuntien lämpötilojen keskiarvo)
    Parametrit:
    raportti (str): 
    """
    alkupv = int(alkupaiva.split(".")[0])
    alkukk = int(alkupaiva.split(".")[1])
    alkuvv = int(alkupaiva.split(".")[2])   
    alku = date(alkuvv, alkukk, alkupv)
    loppupv = int(loppupaiva.split(".")[0])
    loppukk = int(loppupaiva.split(".")[1])   
    loppuvv = int(loppupaiva.split(".")[2])
    loppu = date(loppuvv, loppukk, loppupv)
    kulutus = 0
    tuotanto = 0
    lampotila = 0 
    tietue_lkm = 0 

    for tietue in tietokanta:
        if alku <= tietue[0].date() <= loppu:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1
    
    otsikko = f"Raportti aikaväliltä: {alkupaiva}-{loppupaiva}"
    return muotoile_raportti(otsikko, kulutus, tuotanto, lampotila, tietue_lkm)

def raportti_kk(kuukausi: str, tietokanta: list) -> str:
    """
    Raporttiin tulostetaan:
    - Kuukausi 
    - Kuukauden kokonaiskulutus (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Kuukauden kokonaistuotanto (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Kuukauden keskimääräinen vuorokauden lämpötila

    Parametrit:
    raportti (str): raporttiteksti
    """
    kuukaudet = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu","Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
    
    kuukausi = int(kuukausi)
    kulutus = 0
    tuotanto = 0    
    lampotila = 0
    tietue_lkm = 0

    for tietue in tietokanta:
        if tietue[0].date().month == kuukausi:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1

    otsikko = f"Raportti kuukaudelta: {kuukaudet[kuukausi - 1]}\n"
    return muotoile_raportti(otsikko, kulutus, tuotanto, lampotila, tietue_lkm)

def raportti_vuosi(tietokanta: list) -> str:
    """
    Raporttiin tulostetaan:
    - Kuukausi
    - Kuukauden kokonaiskulutus (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Kuukauden kokonaistuotanto (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Kuukauden keskimääräinen vuorokauden lämpötila

    Parametrit:
    raportti (str): raporttiteksti
    """
    kulutus = 0 
    tuotanto = 0        
    lampotila = 0
    tietue_lkm = 0

    for tietue in tietokanta:
        kulutus += tietue[1]
        tuotanto += tietue[2]
        lampotila += tietue[3]
        tietue_lkm += 1
        

    otsikko = f"Raportti vuodelta 2025\n"
    return muotoile_raportti(otsikko, kulutus, tuotanto, lampotila, tietue_lkm)

def main():
    """
    Ohjelman pääfunktio: kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    kulutus_Tuotanto2025 = lue_date("2025.csv")

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")

        ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alku päivämäärä (pp.kk.vvvv): ")
            loppupaiva = input("Anna loppu päivämäärä (pp.kk.vvvv): ")
            raportti = raportti_aikavali(alkupaiva, loppupaiva, kulutus_Tuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 2:
            kuukausi = (input("Anna kuukausi numerona (1-12): "))
            raportti = raportti_kk(kuukausi, kulutus_Tuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 3:
            raportti = raportti_vuosi(kulutus_Tuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 4:
            print("Ohjelma lopetettu.")
            break
        else:
            continue

        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3):"))
        if toinen_valinta == 1:
            raportti_tiedostoon(raportti)
            print("Raportti kirjoitettu tiedostoon.")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Ohjelma lopetettu.")
            break
        else:
            continue

        print("---------------------------------------------------")       

if __name__ == "__main__":
    main()