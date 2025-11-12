from datetime import datetime

def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

    def main():
        varaukset = "varaukset.txt"

        with open(varaukset, "r", encoding="utf-8") as f:
            varaus = f.read().strip()
            varaus = varaus.split('|')

            hae_varaaja(varaus)
            

    if __name__ == "__main__":
        main()
