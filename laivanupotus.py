# Konsolipohjainen laivanupotuspeli
from random import *
import copy

def tulosta_pelilauta(pelilauta: dict[dict[str, str]]) -> str:
    print("  _A__B__C__D__E_")
    for rivinumero, sarake in pelilauta.items():
        print(f"{rivinumero}| " + "  ".join(sarake[kirjain] for kirjain in sarake) + " |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

def peita_tietokoneen_laivat(pelilauta: dict[int, dict[str, str]]) -> str:
    for rivi, sarake in pelilauta.items():
        for sarake, arvo in sarake.items():
            if arvo == "L":
                pelilauta[rivi][sarake] = "~"
    return pelilauta

def luo_pelilauta() -> dict[int, dict[str, str]]:
    """
    luo pelilaudan
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
    tulosta_pelilauta(pelaaja)
    print("\nVastustajan pelilauta:")
    tietokone_display = copy.deepcopy(tietokone)
    com_tuloste = peita_tietokoneen_laivat(tietokone_display)
    tulosta_pelilauta(com_tuloste)

def laivojen_maara(pelilauta: dict[int, dict[str, str]]) -> int:
    laivat = 0
    for rivi, sarake in pelilauta.items():
        for sarake, arvo in sarake.items():
            if arvo == "L":
                laivat += 1
    return laivat

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
                    print(f"Koordinaatti {laivan_sarake}{laivan_rivi} on jo varattu")
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
            if sarake in "ABCDE" and rivi >= 1 and rivi <= 5:
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
    while i < 5:
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
            ammus = input("Mihin haluat ampua? Esim. A1 tai d3: ").upper()
            tarkistus = tarkista_syote(ammus)
            if tarkistus == "ok":
                rivi = int(ammus[1])
                sarake = ammus[0]
                if pelilauta[rivi][sarake] == "~":
                    pelilauta[rivi][sarake] = "X"
                    print("\nOhi meni!")
                    return pelilauta
                elif pelilauta[rivi][sarake] == "L":
                    pelilauta[rivi][sarake] = "O"
                    print("\nOsuma!")
                    return pelilauta
                else:
                    print("Olet jo ampunut tähän kohtaan.")
            else:
                print("Syötä koordinaatti oikeassa muodossa, esim B4 tai c2.")
        except Exception as e:
            print(f"Jokin meni pieleen syötteessäsi. Error: {e}")

def tietokoneen_ampumakohde(pelilauta):
    i = 0
    while i < 1:
        laivan_rivi = randint(1,5)
        sarake = ["A", "B", "C", "D", "E"]
        sarake_index = randint(0,4)
        laivan_sarake = sarake[sarake_index]
        if pelilauta[laivan_rivi][laivan_sarake] == "~":
            pelilauta[laivan_rivi][laivan_sarake] = "X"
            i += 1
        elif pelilauta[laivan_rivi][laivan_sarake] == "L":
            pelilauta[laivan_rivi][laivan_sarake] = "O"
            i += 1
        else:
            continue

def main():
    """
    pääohjelma:

    """
    kierros = 0
    pelaajan_pelilauta = luo_pelilauta()
    tietokoneen_pelilauta = luo_pelilauta()
    pelitilanne(pelaajan_pelilauta, luo_pelilauta())
    tietokoneen_laivojen_sijainti(tietokoneen_pelilauta)
    keraa_laivojen_sijainnit(pelaajan_pelilauta)
    while True:
        com_laivojen_maara = laivojen_maara(tietokoneen_pelilauta)
        pel_laivojen_maara = laivojen_maara(pelaajan_pelilauta)
        kierros += 1
        print(f"Kierros {kierros}\n")
        if com_laivojen_maara == 0 or pel_laivojen_maara == 0:
            if com_laivojen_maara == 0:
                pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
                print(f"Onnittelut! Voitit pelin! Sinulle jäi vielä {pel_laivojen_maara} laivaa!")
            elif com_laivojen_maara == 0 and pel_laivojen_maara == 0:
                pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
                print("Tasapeli! Olipas tasainen peli!")
            else:
                pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
                print(f"Hävisit pelin! Parempi onni ensi kerralla. Vastustajalle jäi vielä {com_laivojen_maara} laivaa.")
            break
        else:
            pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
            kysy_ampumakohde(tietokoneen_pelilauta)
            tietokoneen_ampumakohde(pelaajan_pelilauta)

if __name__ == "__main__":
    main()