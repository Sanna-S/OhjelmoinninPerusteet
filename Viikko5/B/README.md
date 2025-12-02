# Tehtävän pipeline

1. Luetaan tiedostot

```py
    kulutusTuotantoViikko41 = lue_data("viikko41.csv")
    kulutusTuotantoViikko42 = lue_data("viikko42.csv")
    kulutusTuotantoViikko43 = lue_data("viikko43.csv")
```

2. Tiedot ovat oikean tyyppiset

```py
    print("Viikko41")
    print("-----------")
    print(kulutusTuotantoViikko41[0])
    for i ,arvo in enumerate(kulutusTuotantoViikko41[0]):
        print(f"Indeksi {i}: {arvo} -> {type(arvo)}")
    print("Viikko42")
    print("-----------")
    print(kulutusTuotantoViikko42[0])
    for i ,arvo in enumerate(kulutusTuotantoViikko42[0]):
        print(f"Indeksi {i}: {arvo} -> {type(arvo)}")
    print("Viikko43")
    print("-----------")
    print(kulutusTuotantoViikko43[0])
    for i ,arvo in enumerate(kulutusTuotantoViikko43[0]):
        print(f"Indeksi {i}: {arvo} -> {type(arvo)}")
```

3. Raportoidaan tiedostoista jotain (konsoli)

```py
    # Viikko 41
    print("\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n")
    print("Päivä\t\t\t\tPvm\t\t\t\tKulutus [kWh]\t\t\t\t\t\tTuotanto [kWh]\n")
    print("\t\t\t\t\t(pv.kk.vv)\t\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n")
    print("-" * 101 + "\n")
    print("Maanantai\t\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 6), kulutusTuotantoViikko41)) + "\n")
    print("-" * 101 + "\n")
    # Viikko 42
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n")
    print("Päivä\t\t\t\tPvm\t\t\t\tKulutus [kWh]\t\t\t\t\t\tTuotanto [kWh]\n")
    print("\t\t\t\t\t(pv.kk.vv)\t\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n")
    print("-" * 101 + "\n")
    print("Maanantai\t\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 13), kulutusTuotantoViikko42)) + "\n")
    print("-" * 101 + "\n")
     # Viikko 43
    print("\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n")
    print("Päivä\t\t\t\tPvm\t\t\t\tKulutus [kWh]\t\t\t\t\t\tTuotanto [kWh]\n")
    print("\t\t\t\t\t(pv.kk.vv)\t\tv1\t\t\tv2\t\t\tv3\t\t\tv1\t\t\tv2\t\t\tv3\n")
    print("-" * 101 + "\n")
    rint("Maanantai\t\t\t" + "\t\t".join(paivantiedot(date(2025, 10, 20), kulutusTuotantoViikko42)) + "\n")
    print("-" * 101 + "\n")
```
4. Kirjoitetaan tiedostoon jotain 

```py
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write("Sähkönkulutus ja -tuotanto viikoittain\n")
```
5. Kirjoitetaan tiedostoon raportin pohja.

```py
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
        # Tasataan viikonpäivän nimi 11 merkkiin, jotta päivämäärä alkaa samasta kohdasta
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
    Yhteenveto += "-" * 30 + "\n"
    Yhteenveto += f"Viikko 41 - Kulutus: {kulutus41:.2f} kWh, Tuotanto: {tuotanto41:.2f} kWh\n"
    Yhteenveto += f"Viikko 42 - Kulutus: {kulutus42:.2f} kWh, Tuotanto: {tuotanto42:.2f} kWh\n"
    Yhteenveto += f"Viikko 43 - Kulutus: {kulutus43:.2f} kWh, Tuotanto: {tuotanto43:.2f} kWh\n"



    # Kirjoitetaan jotain tiedostoon
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)
        f.write(Yhteenveto)

    print("Raportti luotu")
```