# Copyright (c) 2025 Sanna Sjöblad
# Licence: MIT

from datetime import datetime, date, timedelta

def muunna_tiedot(tietue: list) -> list:
    """
    Muuttaa yhden jokaisen CSV-tiedoston tietorivin tietotyypit oikeiksi.
        
    Parametrit:
        tietue (list): Sisältää 7 merkkijonoa: ensimmäinen date(aika) ja loput int(kokonaislukuja)
        
    Palauttaa: Listan, jossa on muutetut tietotyypit.
    """
    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
    ]

def lue_data(tiedoston_nimi: str) -> list:
    """
    Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypissä.
        -Kutsuu muunna_tiedot-funktiota muuntaakseen jokaisen rivin tietotyypit sopiviksi.
        -Ohittaa ensimmäisen rivin, joka sisältää sarakkeiden esittelytiedot.

    Parametrit:
        tiedoston_nimi (str): Luettavan tiedoston nimi, ottaa vastaan tiedoston jossa kentät on erotettu puolipisteellä

    Palauttaa: 
        list: Lista, jossa on jokainen rivion muunnettu oikeaan tietotyyppiin.
    """
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
    Laskee annetun päivän kulutukset ja tuotannot vaiheittain.
    Laskee kulutuksen ja tuotannon kolmessa vaiheessa erikseen ja muuntaa ne kWh:ksi jakamalla luvut tuhannella.
    Muotoilee pvm-merkkijonon muodossa "pp.kk.vvvv" ja desimaalierottimen pilkuksi.

    Parametrit:
        paiva (date): Päivämäärä, jolta tiedot lasketaan
        tietokanta (list): kaikki viikon rivit, joissa on päivämäärä, kulutus ja tuotanto

    Palauttaa: Lista, jossa on pvm-merkkijono ja kuusi kulutus- ja tuotantolukemaa merkkijonoina.
    """
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for tietue in tietokanta:
        if tietue[0].date() == paiva:
            kulutus[0] += tietue[1] / 1000
            kulutus[1] += tietue[2] / 1000
            kulutus[2] += tietue[3] / 1000
            tuotanto[0] += tietue[4] / 1000
            tuotanto[1] += tietue[5] / 1000
            tuotanto[2] += tietue[6] / 1000

    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    ]

def laske_yhteenvedot(tietokanta: list) -> list:
    """
    Laskee koko viikon kulutuksen ja tuotannon yhteen.

    Parametrit:
        tietokanta (list): kaikki viikon rivit, joissa on päivämäärä, kulutus ja tuotanto

    Palauttaa: 
        Lista, jossa on viikon kokonaiskulutus ja -tuotanto kWh:na.
    """
    kulutus = tuotanto = 0.0
    for tietue in tietokanta:
        kulutus += (tietue[1] + tietue[2] + tietue[3]) / 1000
        tuotanto += (tietue[4] + tietue[5] + tietue[6]) / 1000

    return [kulutus, tuotanto]

def main():
    """
    Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin.
        -Lukee viikkojen 41-43 CSV-tiedostot lue_data-funktiolla
        -Tulostaa otsikon ja taulukon sarakkeet
        -Tulostaa ensimmäisen maanantain tiedot erikseen
        -Käyttää silmukkaa ensimmäisen viikon tiistaista sunnuntaihin sekä viikkojen 42 ja 43 kaikkiin päiviin
        -Laskee kullekkin päivälle kulutuksen ja tuotannon vaiheittaisen paivantiedot-funktiolla
        -Tulostaa taulukon, joissa näkyy kunkin päivän nimi, päivämäärä, kulutus ja tuotanto vaiheittain
        -Laskee viikon yhteenvedot laske_yhteenvedot-funktiolla
        -Kirjoittaa raportin tiedostoon "yhteenveto.txt"
"""
    kulutusTuotantoViikko41 = lue_data("viikko41.csv")
    kulutusTuotantoViikko42 = lue_data("viikko42.csv")
    kulutusTuotantoViikko43 = lue_data("viikko43.csv")
    # Viikko 41
    viikko41 = "\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko41 += "Päivä\t\t\t\tPvm\t\t\t\tKulutus [kWh]\t\t\t\t\t\tTuotanto [kWh]\n"
    viikko41 += "\t\t\t\t\t(pv.kk.vv)\t\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n"
    viikko41 += "-" * 101 + "\n" # luo merkkijonon, jossa on 101 viivaa. Tulostaa vaakaviivan taulukkoon
    viikko41 += "Maanantai\t\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 6), kulutusTuotantoViikko41)) + "\n"
    viikonpaivat = ["Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    alku = date(2025, 10, 7)  # Tiistai

    for i, nimi in enumerate(viikonpaivat):
        paiva = alku + timedelta(days=i)
        tiedot = paivantiedot(paiva, kulutusTuotantoViikko41)
        # Tasataan viikonpäivän nimi 20 merkin levyiseksi, jotta taulukko pysyy siistinä
        viikko41 += f"{nimi:<20}" + "\t\t".join(tiedot) + "\n"
    viikko41 += "-" * 101 + "\n"

    # Viikko 42
    viikko42 = "\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko42 += "Päivä\t\t\t\tPvm\t\t\t\tKulutus [kWh]\t\t\t\t\t\tTuotanto [kWh]\n"
    viikko42 += "\t\t\t\t\t(pv.kk.vv)\t\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n"
    viikko42 += "-" * 101 + "\n"
    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    alku = date(2025, 10, 13)
    
    for i, nimi in enumerate(viikonpaivat):
        paiva = alku + timedelta(days=i)
        tiedot = paivantiedot(paiva, kulutusTuotantoViikko42)
        viikko42 += f"{nimi:<20}" + "\t\t".join(tiedot) + "\n"
    viikko42 += "-" * 101 + "\n"

   # Viikko 43
    viikko43 = "\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko43 += "Päivä\t\t\t\tPvm\t\t\t\tKulutus [kWh]\t\t\t\t\t\tTuotanto [kWh]\n"
    viikko43 += "\t\t\t\t\t(pv.kk.vv)\t\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n"
    viikko43 += "-" * 101 + "\n"
    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    alku = date(2025, 10, 20)

    for i, nimi in enumerate(viikonpaivat):
        paiva = alku + timedelta(days=i)
        tiedot = paivantiedot(paiva, kulutusTuotantoViikko43)
        viikko43 += f"{nimi:<20}" + "\t\t".join(tiedot) + "\n"
    viikko43 += "-" * 101 + "\n"

    # Lasketaan yhteenvedot tiedostoon

    kulutus41, tuotanto41 = laske_yhteenvedot(kulutusTuotantoViikko41)
    kulutus42, tuotanto42 = laske_yhteenvedot(kulutusTuotantoViikko42)
    kulutus43, tuotanto43 = laske_yhteenvedot(kulutusTuotantoViikko43)

    Yhteenveto = "\nViikkojen yhteenveto (kWh):\n"
    Yhteenveto += "-" * 53 + "\n"
    Yhteenveto += f"Viikko 41 - Kulutus: {kulutus41:.2f} kWh, Tuotanto: {tuotanto41:.2f} kWh\n"
    Yhteenveto += f"Viikko 42 - Kulutus: {kulutus42:.2f} kWh, Tuotanto: {tuotanto42:.2f} kWh\n"
    Yhteenveto += f"Viikko 43 - Kulutus: {kulutus43:.2f} kWh, Tuotanto: {tuotanto43:.2f} kWh\n"
    Yhteenveto += "-" * 53 + "\n"
    
    # Kirjoitetaan jotain tiedostoon
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)
        f.write(Yhteenveto) 

    print("Raportti luotu")
    

    
        
if __name__ == "__main__":
    main()