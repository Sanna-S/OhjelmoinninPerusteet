from datetime import datetime

def hae_varausnumero(varaus):
    nimi = varaus[0]
    print(f"Varausnumero: {nimi}")

def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

def hae_paiva(varaus):
    nimi = varaus[2]
    paiva = datetime.strptime(nimi, "%Y-%m-%d")
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    print(f"Päivämäärä: {suomalainenPaiva}")

def hae_aloitusaika(varaus):
    nimi = varaus[3]
    aika = datetime.strptime(nimi, "%H:%M")
    suomalainenAika = aika.strftime("%H.%M")
    print(f"Aloitusaika: {suomalainenAika}")    
    
def hae_tuntimaara(varaus):
    nimi = varaus[4]
    print(f"Tuntimäärä: {nimi}")  
 
def hae_tuntihinta(varaus):
    nimi = varaus[5]
    hinta = float(nimi)
    hinta_str = f"{hinta:.2f}".replace('.', ',')
    print(f"Tuntihinta: {hinta_str} €")   
  
def laske_kokonaishinta(varaus):
    nimi = varaus[4]
    tuntimaara = float(nimi)
    nimi2 = varaus[5]
    tuntihinta = float(nimi2)
    kokonaishinta = tuntimaara * tuntihinta
    hinta_str = f"{kokonaishinta:.2f}".replace('.', ',').rstrip('0').rstrip(',')
    print(f"Kokonaishinta: {hinta_str} €")

def hae_maksettu(varaus):
    nimi = varaus[6]
    if nimi == "True":
        print("Maksettu: Kyllä")
    else:
        print("Maksettu: Ei")

def hae_kohde(varaus):
    nimi = varaus[7]
    print(f"Kohde: {nimi}")

def hae_puhelin(varaus):
    nimi = varaus[8]
    print(f"Puhelin: {nimi}") 

def hae_sahkoposti(varaus):
    nimi = varaus[9]
    print(f"Sähköposti: {nimi}")   

def main():
    varaukset = "varaukset.txt"

    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    


    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)
            

if __name__ == "__main__":
    main()
