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
4. Kirjoitetaan tiedostoon jotain 
5. Kirjoitetaan tiedostoon raportin pohja.