# Copyright (c) 2025 Sanna Sjöblad
# Licence: MIT

from datetime import datetime, date

def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa yhden jokaisen CSV-tiedoston tietorivin tietotyypit oikeiksi.
        
    Parametrit:
        tietue (list): Sisältää 7 merkkijonoa: ensimmäinen date(aika) ja loput int(kokonaislukuja)
        
    Palauttaa: Listan, jossa on muutetut tietotyypit.
    """
    muutettu__tietorivi = []
    muutettu__tietorivi.append(datetime.fromisoformat(tietue[0]))  
    muutettu__tietorivi.append(int(tietue[1])) 
    muutettu__tietorivi.append(int(tietue[2]))  
    muutettu__tietorivi.append(int(tietue[3]))  
    muutettu__tietorivi.append(int(tietue[4]))
    muutettu__tietorivi.append(int(tietue[5]))
    muutettu__tietorivi.append(int(tietue[6]))
    return muutettu__tietorivi


def lue_data(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypissä.
        -avaa tiedoston, jossa on sarakkeet eroteltu puolipisteillä
        -ohittaa ensimmäisen rivin (sarakkeiden esittelyrivin)
        -muuntaa jokaisen rivin tietotyypit oikeiksi kutsumalla muunna_tiedot-funktiota

    Parametrit:
        tiedoston_nimi (str): Luettavan tiedoston nimi
    
    Palauttaa: Lista, jossa on jokainen tietue listana sopivilla tietotyypeillä."""
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Ohitetaan sarakkaiden esittelyrivi pois
        for tietue in f:
            tietue = tietue.strip()
            tietueSarakkeet = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietueSarakkeet))
    return tietokanta


def paivantiedot(paiva: date, tietokanta: list) -> list:
    """
    Laskee annetun päivän kulutukset ja tuotannot vaiheittain yhteen.
    Laskee kulutuksen ja tuotannon kolmessa vaiheessa erikseen ja muuntaa ne kWh:ksi jakamalla luvut tuhannella.
    Muotoilee pvm-merkkijonon muodossa "pp.kk.vvvv" ja desimaalierottimen pilkuksi.

    Parametrit:
        paiva (date): Päivämäärä, jolta tiedot lasketaan
        tietokanta (list): kaikki viikon rivit, joissa on päivämäärä, kulutus ja tuotanto

    Palauttaa: Lista, jossa on pvm-merkkijono ja kuusi kulutus- ja tuotantolukemaa merkkijonoina.
    """
    kulutus1 = kulutus2 = kulutus3 = 0
    tuotanto1 = tuotanto2 = tuotanto3 = 0

    for lukema in tietokanta:
        if lukema[0].date() == paiva:
            kulutus1 += lukema[1] / 1000  # Muutetaan kWh:ksi
            kulutus2 += lukema[2] / 1000
            kulutus3 += lukema[3] / 1000
            tuotanto1 += lukema[4] / 1000
            tuotanto2 += lukema[5] / 1000
            tuotanto3 += lukema[6] / 1000

    pvm_str = f"{paiva.day:02d}.{paiva.month:02d}.{paiva.year}"
    
    return [
        pvm_str,
        f"{kulutus1:.2f}".replace(".", ","),
        f"{kulutus2:.2f}".replace(".", ","),
        f"{kulutus3:.2f}".replace(".", ","),
        f"{tuotanto1:.2f}".replace(".", ","),
        f"{tuotanto2:.2f}".replace(".", ","),
        f"{tuotanto3:.2f}".replace(".", ","),
    ]

def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
        -Lukee CSV-tiedoston lue_data-funktiolla
        -Tulostaa otsikon ja taulukon sarakkeet
        -Tulostaa jokaisen viikonpäivän erikseen
        -Laskee kullekkin päivälle kulutuksen ja tuotannon vaiheittaisen paivantiedot-funktiolla
        -Tulostaa taulukon, joissa näkyy kunkin päivän nimi, päivämäärä, kulutus ja tuotanto vaiheittain
"""
    tietokanta = lue_data("viikko42.csv")
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 13), tietokanta)))
    print("Tiistai\t\t" + "\t".join(paivantiedot(date(2025, 10, 14), tietokanta)))
    print("Keskiviikko\t" + "\t".join(paivantiedot(date(2025, 10, 15), tietokanta)))
    print("Torstai\t\t" + "\t".join(paivantiedot(date(2025, 10, 16), tietokanta)))
    print("Perjantai\t" + "\t".join(paivantiedot(date(2025, 10, 17), tietokanta)))
    print("Lauantai\t" + "\t".join(paivantiedot(date(2025, 10, 18), tietokanta)))
    print("Sunnuntai\t" + "\t".join(paivantiedot(date(2025, 10, 19), tietokanta)))

    
        
if __name__ == "__main__":
    main()