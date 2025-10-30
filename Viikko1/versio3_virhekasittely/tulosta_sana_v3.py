def main():
    tiedosto = "sana.txt"
    try:
        with open(tiedosto, "r" , encoding="utf-8") as f:
            sana = f.read().strip()

        if not sana:
            print("Virhe: Tiedosto on tyhjä.")
            return
        print(sana)
    except FileNotFoundError:
                print(f"Virhe: Tiedostoa '{tiedosto}' ei löytynyt.")
    except PermissionError:
            print(f"Virhe: Tiedostoon '{tiedosto}' ei ole oikeuksia.")
    except Exception as e:
            print(f"Virhe: {e}")    
        
if __name__ == "__main__":
        main()
