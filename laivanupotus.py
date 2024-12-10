# Konsolipohjainen laivanupotuspeli
from random import *
import copy
import os

def clear_console():
    # Tyhjentää konsolin vanhoista tulosteista käyttöjärjestelmästä riippumatta
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def luo_pelilauta() -> dict[int, dict[str, str]]:
    """
    luo pelilaudan

    pelilauta koostuu sisäkkäisistä sanakirjoista, joiden arvoja muuttamalla pelikenttä muuttuu
    """
    pelilauta = {
        1: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        2: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        3: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        4: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"},
        5: {"A": "~", "B": "~", "C": "~", "D": "~", "E": "~"}
    }
    return pelilauta

def tietokoneen_laivojen_sijainti(pelilauta: dict[int, dict[str, str]]) -> dict[int, dict[str, str]]:
    # arpoo 5 tietokoneen laivaa ja sijoittaa ne pelilaudalle
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

def keraa_laivojen_sijainnit(pelilauta: dict[int, dict[str, str]]) -> dict[int, dict[str, str]]:
    """
    funtio pelaajan laivojen sijoittamiseen

    ottaa parametrinä pelaajan pelilaudan
    ottaa vastaan syötteenä koordinaatit laivoille
    tarkistaa syötteen tarkista_syote funktion avulla
    sijoittaa 5 laivaa syötettyihin koordinaatteihin
    """
    laivat = 0
    while laivat < 5:
        try:
            print(f"Sijoita vielä {5 - laivat} laiva(a).")
            tulosta_pelilauta(pelilauta)
            laiva = input("Syötä laivan sijainti (esim. A1): ").upper()
            tarkistus = tarkista_syote(laiva)
            clear_console()
            if tarkistus == "ok":
                laivan_rivi = int(laiva[1])
                laivan_sarake = laiva[0]
                if pelilauta[laivan_rivi][laivan_sarake] == "~":
                    pelilauta[laivan_rivi][laivan_sarake] = "L"
                    laivat += 1
                else:
                    print(f"Koordinaatti {laivan_sarake}{laivan_rivi} on jo varattu")
            elif tarkistus == "ei koordinaatistossa":
                print(f"{laiva} ei ole koordinaatistossa.")
            elif tarkistus == "not ok":
                print("Syötä koordinaatti oikeassa muodossa, esim B4.")
            else:
                print(tarkistus)
        except Exception as e:
            print(f"Jokin meni pieleen syötteessäsi. Error: {e}")
    return pelilauta

def tarkista_syote(syote: str) -> str:
    """
    funktio käyttäjän syötteen tarkastamiseen

    tarkistaa:
        - onko syöte halutun pituinen
        - onko syöte koordinaatistolla
    
    palauttaa tarkistuksen tuloksen
    """
    try:
        if len(syote) == 2:
            rivi = int(syote[1])
            sarake = syote[0]
            if sarake in "ABCDE" and rivi >= 1 and rivi <= 5:
                return "ok"
            elif sarake.isalpha():
                return "ei koordinaatistossa"
            else:
                return "not ok"
        else:
            return "not ok"
    except Exception as e:
        return f"Jokin meni pieleen syötteessäsi. Error: {e}"

def laivojen_maara(pelilauta: dict[int, dict[str, str]]) -> int:
    """
    funktio jäljellä olevien laivojen määrän laskemiseen

    parametrina annetaan pelaajan tai tietokoneen pelilauta

    laskee laivat ja palauttaa niiden lukumäärän
    """
    laivat = 0
    for rivi, sarake in pelilauta.items():
        for sarake, arvo in sarake.items():
            if arvo == "L":
                laivat += 1
    return laivat

def pelitilanne(pelaaja: dict[int, dict[str, str]], tietokone: dict[int, dict[str, str]]) -> None:
    """
    funktio tämänhetkisen pelitilanteen tulostamiseen
    
    käyttää tulosta_pelilauta funktiota molempien pelilautojen tulostamiseen

    luo tietokoneen pelilaudasta kopion, joka ei muuta alkuperäistä lautaa, jotta pelaaja ei näe laivoja
    tulostaa tietokoneen pelilaudan ilman laivoja
    """
    print("Sinun pelilautasi:")
    tulosta_pelilauta(pelaaja)
    print("\nVastustajan pelilauta:")
    tietokone_display = copy.deepcopy(tietokone)
    com_tuloste = peita_tietokoneen_laivat(tietokone_display)
    tulosta_pelilauta(com_tuloste)

def tulosta_pelilauta(pelilauta: dict[dict[str, str]]) -> None:
    """
    funktio pelilaudan tulostamista varten

    käy läpi parametrina annetun pelilaudan ja tulostaa sen arvot halutulla tavalla
    """
    print("  _A__B__C__D__E_")
    for rivinumero, sarake in pelilauta.items():
        print(f"{rivinumero}| " + "  ".join(sarake[kirjain] for kirjain in sarake) + " |")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

def peita_tietokoneen_laivat(pelilauta: dict[int, dict[str, str]]) -> dict[int, dict[str, str]]:
    """
    ottaa vastaan parametrina kopion tietokoneen pelilaudasta

    muuttaa pelilaudan laivat "näkymättömiksi" 
    """
    for rivi, sarake in pelilauta.items():
        for sarake, arvo in sarake.items():
            if arvo == "L":
                pelilauta[rivi][sarake] = "~"
    return pelilauta

def kysy_ampumakohde(pelilauta: dict[int, list[str]]) -> dict[int, dict[str, str]]:
    """
    funktio pelaajan ampumiskoordinaatin kysymiseen

    käyttää funktiota tarkista_syote funktiota syötteen tarkistukseen

    muuttaa tulostetta tarkistuksen tuloksen mukaan
    """
    while True:
        try:
            ammus = input("Mihin haluat ampua? Esim. A1 tai d3: ").upper()
            tarkistus = tarkista_syote(ammus)
            if tarkistus == "ok":
                rivi = int(ammus[1])
                sarake = ammus[0]
                if pelilauta[rivi][sarake] == "~":
                    pelilauta[rivi][sarake] = "X"
                    clear_console()
                    print("Ohi meni!")
                    return pelilauta
                elif pelilauta[rivi][sarake] == "L":
                    pelilauta[rivi][sarake] = "O"
                    clear_console()
                    print("Osuma!")
                    return pelilauta
                else:
                    print("Olet jo ampunut tähän kohtaan.")
            elif tarkistus == "ei koordinaatistossa":
                print(f"{ammus} ei ole koordinaatistossa.")
            elif tarkistus == "not ok":
                print("Syötä koordinaatti oikeassa muodossa, esim B4 tai c2.")
            else:
                print(tarkistus)
        except Exception as e:
            print(f"Jokin meni pieleen syötteessäsi. Error: {e}")

def tietokoneen_ampumakohde(pelilauta: dict[int, dict[str, str]]) -> dict[int, dict[str, str]]:
    """
    arpoo koordinaatin pelilaudalta, kunnes löytyy tyhjä tai laivan omaava koordinaatti

    muuttaa tietokoneen pelilautaa sen mukaan oliko koordinaatissa laiva vai ei
    """
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

    tyhjentää aluksi terminaalin, jotta peli näkyy halutulla tavalla

    luo pelaajalle ja tietokoneelle pelilaudat

    kerää laivojen sijainnit käyttäen tietokoneen_laivojen_sijainti ja keraa_laivojen_sijainti -funktioita

    laskee laivojen määrän ja lopettaa pelin jos ainakin toiselta tuhotaan kaikki laivat

    joka kierroksen jälkeen tyhjentää konsolin

    käyttää pelitilanne funtiota näyttääkseen nykyisen tilanteen

    kysyy joka kierroksella pelaajalta ampumakoordinaatin käyttäen kysy_ampumakohde funktiota

    arpoo tietokoneen ampumakohteen käyttäen tietokoneen_ampumakohde funktiota

    pelin päätyttyä tuloste muuttuu lopputuloksen mukaan
    """
    clear_console()
    kierros = 0
    pelaajan_pelilauta = luo_pelilauta()
    tietokoneen_pelilauta = luo_pelilauta()
    tietokoneen_laivojen_sijainti(tietokoneen_pelilauta)
    keraa_laivojen_sijainnit(pelaajan_pelilauta)
    clear_console()
    while True:
        com_laivojen_maara = laivojen_maara(tietokoneen_pelilauta)
        pel_laivojen_maara = laivojen_maara(pelaajan_pelilauta)
        kierros += 1
        print(f"Kierros {kierros}\n")
        if com_laivojen_maara == 0 or pel_laivojen_maara == 0:
            if com_laivojen_maara == 0:
                pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
                print(f"Onnittelut! Voitit pelin! Sinulle jäi vielä {pel_laivojen_maara} laiva(a)!")
            elif com_laivojen_maara == 0 and pel_laivojen_maara == 0:
                pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
                print("Tasapeli! Olipas tasainen peli!")
            else:
                pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
                print(f"Hävisit pelin! Parempi onni ensi kerralla. Vastustajalle jäi vielä {com_laivojen_maara} laiva(a).")
            break
        else:
            pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta)
            kysy_ampumakohde(tietokoneen_pelilauta)
            tietokoneen_ampumakohde(pelaajan_pelilauta)

if __name__ == "__main__":
    main()