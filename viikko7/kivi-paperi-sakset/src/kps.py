from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        while True:
            ekan_siirto = self._ekan_siirto()
            if not self._onko_ok_siirto(ekan_siirto):
                break
            tokan_siirto = self._tokan_siirto(ekan_siirto)
            if not self._onko_ok_siirto(tokan_siirto):
                break
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)


        print("Kiitos!")
        print(tuomari)

    def _ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_siirto(self, siirto):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly1 = Tekoaly()

    def _tokan_siirto(self, siirto):
        tokan_siirto = self.tekoaly1.anna_siirto()
        print(f"Toisen pelaajan siirto: {tokan_siirto}")
        return tokan_siirto

class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly2 = TekoalyParannettu(10)

    def _tokan_siirto(self, siirto):
        tokan_siirto = self.tekoaly2.anna_siirto()
        self.tekoaly2.aseta_siirto(siirto)
        print(f"Toisen pelaajan siirto: {tokan_siirto}")
        return tokan_siirto

