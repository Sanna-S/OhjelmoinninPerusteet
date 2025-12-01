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
    print("\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("----------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 6), kulutusTuotantoViikko41)))
    print("---------------------------------------------------------------------------")
    # Viikko 42
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("----------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 13), kulutusTuotantoViikko42)))
    print("----------------------------------------------------------------------------")
     # Viikko 43
    print("\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("----------------------------------------------------------------------------")
    print("Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 20), kulutusTuotantoViikko43)))
    print("----------------------------------------------------------------------------")
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
    viikko41 += "Päivä\t\tPvm\t\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko41 += "\t\t\t(pv.kk.vvvv)\t\tv1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko41 += "----------------------------------------------------------------------------\n"
    viikko41 += "Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 6), kulutusTuotantoViikko41)) + "\n"
    viikko41 += "---------------------------------------------------------------------------\n"
    # Viikko 42
    viikko42 = "\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko42 += "Päivä\t\tPvm\t\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko42 += "\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\t\tv2\t\tv3\n"
    viikko42 += "----------------------------------------------------------------------------\n"
    viikko42 += "Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 13), kulutusTuotantoViikko42)) + "\n"
    viikko42 += "---------------------------------------------------------------------------\n"
   # Viikko 43
    viikko43 = "\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko43 += "Päivä\t\tPvm\t\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko43 += "\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\t\tv2\t\tv3\n"
    viikko43 += "----------------------------------------------------------------------------\n"
    viikko43 += "Maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 20), kulutusTuotantoViikko43)) + "\n"
    viikko43 += "---------------------------------------------------------------------------\n"
    # Kirjoitetaan jotain tiedostoon
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41+viikko42+viikko43)
        

    print("Raportti luotu")
```