# Konsolipohjainen laivanupotuspeli
from random import *
import string

def tulosta_pelilauta(pelilauta: dict[int, dict[str, str]]) -> str:
    print("  _A__B__C__D__E_")
    for rivinumero, rivi in pelilauta.items():
        print(f"{rivinumero}| " + "  ".join(rivi[sarake] for sarake in "ABCDE") + " |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

def luo_pelilauta() -> dict[int, dict[str, str]]:
    """
    generoi pelilaudan

    Returns:
        sanakirjan sanakirjoja, jotka muodostavat pelilaudan
    """
    pelilauta = {
        1: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        2: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        3: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        4: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        5: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"}
    }
    return pelilauta

def pelitilanne(pelaaja, tietokone):
    print("Sinun pelilautasi:")
    print(tulosta_pelilauta(pelaaja))
    print("\nVastustajan pelilauta:")
    print(tulosta_pelilauta(tietokone))

def pelaajan_tilanne(pelilauta, laivat, osumat):
    pass

def tietokoneen_tilanne(pelilauta, laivat, osumat):
    pass

def keraa_laivojen_sijainnit(pelilauta: dict[int, dict[str, str]]):
    """
    ottaa vastaan syötteenä koordinaatit laivoille

    tarkistaa syötteen tarkista_syote funktion avulla

    sijoittaa laivat haluttuihin koordinaatteihin pelitilanne funktion avulla
    """
    laivat = 0
    while laivat < 5:
        try:
            laiva = input("Syötä laivan sijainti (esim. A1): ").upper()
            tarkistus = tarkista_syote(laiva)
            if tarkistus == "ok":
                laivan_rivi = int(laiva[1])
                laivan_sarake = laiva[0]
                if pelilauta[laivan_rivi][laivan_sarake] == "~":
                    pelilauta[laivan_rivi][laivan_sarake] = "L"
                    laivat += 1
                else:
                    print(f"Koordinaatti {laivan_rivi}{laivan_sarake} on jo varattu")
            else:
                print("Syötä koordinaatti oikeassa muodossa, esim B4.")
        except Exception as e:
            print(f"Jokin meni pieleen. Error: {e}")
    return pelilauta

def tarkista_syote(syote):
    try:
        if len(syote) == 2:
            rivi = int(syote[1])
            sarake = syote[0]
            if sarake in "ABCDE" and (rivi >= 1 or rivi <= 5):
                return "ok"
        else:
            return "not ok"
    except Exception as e:
        print(f"Jokin meni pieleen. Error: {e}")

def tietokoneen_laivojen_sijainti(pelilauta):
    """
    arpoo tietokoneen laivojen sijainnit ja sijoittaa ne pelilaudalle
    """
    i = 0
    while i in range(5):
        laivan_rivi = randint(1,5)
        sarake = ["A", "B", "C", "D", "E"]
        sarake_index = randint(0,4)
        laivan_sarake = sarake[sarake_index]
        if pelilauta[laivan_rivi][laivan_sarake] == "~":
            pelilauta[laivan_rivi][laivan_sarake] = "L"
            i += 1
        elif pelilauta[laivan_rivi][laivan_sarake] == "L":
            continue

def kysy_ampumakohde(pelilauta: dict[int, list[str]]):
    while True:
        try:
            ammus = input("Mihin haluat ampua? Esim. A1: ").upper()
            tarkistus = tarkista_syote(ammus)
            if tarkistus == "ok":
                rivi = int(ammus[1])
                sarake = ammus[0]
                if pelilauta[rivi][sarake] == "~":
                    pelilauta[rivi][sarake] = "X"
                    return pelilauta
                elif pelilauta[rivi][sarake] == "L":
                    pelilauta[rivi][sarake] = "X"
                    return pelilauta
                else:
                    print("Olet jo ampunut tähän kohtaan.")
            else:
                print("Syötä koordinaatti oikeassa muodossa, esim B4.")
        except Exception as e:
            print(f"Jokin meni pieleen. Error: {e}")

def tarkista_osumat():
    """
    tarkistaa ja merkitsee osuman pelitilanne funktion avulla
    """
    pass

def kierroslaskuri(kierros):
    kierros += 1
    return kierros

def main():
    """
    pääohjelma:

    """
    kierros = 0
    pelaajan_pelilauta = luo_pelilauta()
    tietokoneen_pelilauta = luo_pelilauta()
    pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
    tietokoneen_laivojen_sijainti(tietokoneen_pelilauta)
    keraa_laivojen_sijainnit(pelaajan_pelilauta)
    print(f"Kierros {kierroslaskuri(kierros)}\n")
    pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
    kysy_ampumakohde(tietokoneen_pelilauta)
    print(f"Kierros {kierroslaskuri(kierros)}\n")
    pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)

if __name__ == "__main__":
    main()