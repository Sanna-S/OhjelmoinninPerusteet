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

def raportti_tiedostoon(raportti: str,):
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
    raportti += "-Kokonaiskulutus: " + f"{kulutus:.2f}".replace(".", ",") + " kWh\n"
    raportti += "-Kokonaistuotanto: " + f"{tuotanto:.2f}".replace(".", ",") + " kWh\n"
    raportti += "-Keskilämpötila: " + f"{lampotila/tietue_lkm:.2f}".replace(".", ",") + " °C\n"
    raportti += "-" * 50 + "\n"
    return raportti

def raportti_aikavali(alkupaiva: datetime.date, loppupaiva: datetime.date, tietokanta: list) -> str:
    """
    Raportiin tulostetaan aikaväliltä:
    - Alkupäivämäärä ja loppupäivämäärä (pp.kk.vvvv-pp.kk.vvvv)
    - Aikavälin kokonaiskulutuksen (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Aikavälin kokonaistuotannon (kWh, 2 desimaalin tarkkuudella, pilkku desimaalierottimena)
    - Aikavälin keskilämpötila (°C, esim. kaikkien tuntien lämpötilojen keskiarvo)
    Parametrit:
    raportti (str): raporttiteksti
    """
    kulutus = 0
    tuotanto = 0
    lampotila = 0 
    tietue_lkm = 0 

    for tietue in tietokanta:
        if alkupaiva <= tietue[0].date() <= loppupaiva:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1
    
    otsikko = f"Raportti aikaväliltä: {alkupaiva}-{loppupaiva}"
    return muotoile_raportti(otsikko, kulutus, tuotanto, lampotila, tietue_lkm)

def raportti_kk(kuukausi: int, tietokanta: list) -> str:
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

def valikot (paavalikko: bool, alavalikko: bool) -> list:
    """
    Luo valikot ja palauttaa valinnat listana.

    Parametrit:
    paavalikko (bool): käynnistetään päävalikko
    alavalikko (bool): käynnistetään alavalikko

    Palauttaa:
    valikon_valinnat (str): valikon valinnat yhdistettynä arvoihin
    """
    while True and paavalikko:
        print("-" * 50)
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        print("-" * 50)
        try:
            valinta = int(input("Anna valinta (numero 1-4):"))
            if not 1 <= valinta <= 4:
                raise ValueError
        except:
            print("Valintasi on virheellinen. Anna numero välillä 1-4.")
            continue

        if valinta == 1:
            try:
                alku_pvm = input("Anna alku päivämäärä (pp.kk.vvvv): ").split(".")
                loppu_pvm = input("Anna loppu päivämäärä (pp.kk.vvvv): ").split(".")
                valinnat = [0, 1, date(int(alku_pvm[2]), int(alku_pvm[1]), int(alku_pvm[0])), date(int(loppu_pvm[2]), int(loppu_pvm[1]), int(loppu_pvm[0]))]
                break
            except:
                print("Päivämäärä on väärässä muodossa. Anna päivämäärä muodossa pp.kk.vvvv. Palataan alkuun.")
                continue

        elif valinta == 2:
            try:
                kuukausi = int(input("Anna kuukausi numerona (1-12): "))
                valinnat = [0, 2, kuukausi]
                break
            except:
                print("Virheellinen valinta. Kuukausi pitää antaa numerona välillä 1-12. Palataan alkuun.")
                continue

        elif valinta == 3:
            valinnat = [0, 3]
            break
        elif valinta == 4:
            valinnat = [0, 4]
            break
        else:
            continue

    while True and alavalikko:
        print("-" * 50)
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        print("-" * 50)
        try:
            valinta = int(input("Anna valinta (numero 1-3):"))
            if not 1 <= valinta <= 3:
                raise ValueError
        except: 
            print("Valintasi on virheellinen. Anna numero välillä 1-3.")
            continue
        valinnat = [1, valinta]
        break
    
    return valinnat

    

def main():
    """
    Ohjelman pääfunktio: kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    
    kulutus_Tuotanto2025 = lue_date("2025.csv")

    while True:
        paavalikko = valikot(True, False)
        if paavalikko[1] == 1:
            raportti = raportti_aikavali(paavalikko[2], paavalikko[3], kulutus_Tuotanto2025)
            print(raportti)
        elif paavalikko[1] == 2:
            raportti = raportti_kk(paavalikko[2], kulutus_Tuotanto2025)
            print(raportti)
        elif paavalikko[1] == 3:
            raportti = raportti_vuosi(kulutus_Tuotanto2025)
            print(raportti)
        elif paavalikko[1] == 4:
            break

        alavalikko = valikot(False, True)
        if alavalikko[1] == 1:
            raportti_tiedostoon(raportti)
            continue
        elif alavalikko[1] == 2:
            continue
        elif alavalikko[1] == 3:
            break

if __name__ == "__main__":
    main()