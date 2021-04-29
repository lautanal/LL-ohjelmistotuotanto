import pelinvalinta

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = pelinvalinta.valinta(vastaus)
        if peli is None:
            break
        else:
            peli.pelaa()

if __name__ == "__main__":
    main()
