from kps import KPS, KPSTekoaly, KPSParempiTekoaly

def valinta(vastaus):

    peli = None
    if vastaus.endswith("a"):
        peli = KPS()
    elif vastaus.endswith("b"):
        peli = KPSTekoaly()
    elif vastaus.endswith("c"):
        peli = KPSParempiTekoaly()

    return peli
 