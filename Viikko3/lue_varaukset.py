from datetime import datetime

def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

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
