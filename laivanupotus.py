# Konsolipohjainen laivanupotuspeli
from random import randint
import copy
import os
from contextlib import redirect_stdout

def clear_console() -> None:
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

def saannot() -> None:
    # funtio pelin sääntöjen esittämiseen
    print("Laivanupotus: Pelaat tietokonetta vastaan. \n\nMolemmat sijoittaa aluksi viisi (5) laivaa.")
    print("Tämän jälkeen alkaa itse peli. \n\nAmmut ensin tietokoneen pelilaudalle ja sen jälkeen tietokoneella on tasoittava vuoro.")
    print("Sijoita laivat ja ammu muodossa: kirjain A-E ja numero 1-5. Esim B5. \nVääristä syötteistä ei menetä vuoroa.")
    print("\nPeliä pelataan kunnes ainakin toinen on upottanut vastustajansa laivat.")
    print("Pelin lopuksi voit halutessasi tallentaa pelin nimeämääsi tiedostoon.")
    input("\nPaina Enter päästäksesi eteenpäin.")

def tietokoneen_laivojen_sijainti(pelilauta: dict[int, dict[str, str]]) -> dict[int, dict[str, str]]:
    # arpoo 5 tietokoneen laivaa ja sijoittaa ne pelilaudalle
    i = 0
    sarake = ["A", "B", "C", "D", "E"]
    while i < 5:
        laivan_rivi = randint(1,5)
        sarake_index = randint(0,4)
        laivan_sarake = sarake[sarake_index]
        if pelilauta[laivan_rivi][laivan_sarake] == "~":
            pelilauta[laivan_rivi][laivan_sarake] = "L"
            i += 1
    return pelilauta

def keraa_laivojen_sijainnit(pelilauta: dict[int, dict[str, str]]) -> dict[int, dict[str, str]]:
    """
    funktio pelaajan laivojen sijoittamiseen

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
                    print(f"Olet jo sijoittanut laivan koordinaattiin {laiva}.")
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
        if len(syote) != 2:
            return "not ok"
        sarake = syote[0]
        rivi = syote[1]
        if not sarake.isalpha() or not rivi.isdigit():
            return "not ok"
        rivi = int(rivi)
        if sarake in "ABCDE" and 1 <= rivi <= 5:
            return "ok"
        else:
            return "ei koordinaatistossa"
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

def pelitilanne(pelaaja: dict[int, dict[str, str]], tietokone: dict[int, dict[str, str]], pel_laivat: int, com_laivat: int) -> None:
    """
    funktio tämänhetkisen pelitilanteen tulostamiseen
    
    käyttää tulosta_pelilauta funktiota molempien pelilautojen tulostamiseen

    luo tietokoneen pelilaudasta kopion, joka ei muuta alkuperäistä lautaa, jotta pelaaja ei näe laivoja
    tulostaa tietokoneen pelilaudan ilman laivoja
    """
    print("Sinun pelilautasi:")
    tulosta_pelilauta(pelaaja)
    print(f"Sinun laivoja jäljellä: {pel_laivat}")
    print("\nVastustajan pelilauta:")
    tietokone_display = copy.deepcopy(tietokone)
    peita_tietokoneen_laivat(tietokone_display)
    tulosta_pelilauta(tietokone_display)
    print(f"Tietokoneen laivoja jäljellä: {com_laivat}\n")

def tulosta_pelilauta(pelilauta: dict[dict[str, str]]) -> None:
    """
    funktio pelilaudan tulostamista varten

    käy läpi parametrina annetun pelilaudan ja tulostaa sen arvot halutulla tavalla
    """
    print("  _A__B__C__D__E_")
    for rivinumero, sarake in pelilauta.items():
        print(f"{rivinumero}| " + "  ".join(sarake[arvo] for arvo in sarake) + " |")
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
                    print(f"Osuma! Upotit laivan kohdassa {ammus}!")
                    return pelilauta
                else:
                    print(f"Olet jo ampunut kohtaan {ammus}.")
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
    sarakkeet = ["A", "B", "C", "D", "E"]
    while True:
        rivi = randint(1,5)
        sarake = sarakkeet[randint(0,4)]
        if pelilauta[rivi][sarake] == "~":
            pelilauta[rivi][sarake] = "X"
            print(f"Pelilautasi kohtaan {sarake}{rivi} ammuttiin!\n")
            break
        elif pelilauta[rivi][sarake] == "L":
            pelilauta[rivi][sarake] = "O"
            print(f"Laivasi kohdassa {sarake}{rivi} upposi!\n")
            break
    return pelilauta

def pelin_tallennus(kierros: int, pel: dict[int, dict[str, str]], com: dict[int, dict[str, str]], pel_laivat: int, com_laivat: int) -> None:
    """
    ottaa parametrina vastaan pelitilanne funktion vaatimat parametrit
    ottaa vastaan ja tarkistaa pelaajan antaman tiedostonimen pelin tallennukselle
    käsittelee poikkeukset
    kirjoittaa pelin tiedostoon utf-8 koodauksella, jotta ääkköset ja yläviivat näkyvät oikein
    koska pelitilanne funktio ei palauta mitään, käytetään tiedostoon kirjoituksessa redirect_stdout context manageria
    """
    while True:
        tiedostonimi = input("Anna tallennustiedoston nimi ilman tiedostopäätettä. ")
        if not tiedostonimi.isalnum():
            print("Tiedostonimen tulee olla vain kirjaimia ja numeroita.")
            continue
        if len(tiedostonimi) < 3:
            print("Tiedostonimen tulee olla ainakin 3 merkkiä pitkä.")
            continue
        try:
            tiedostopolku = os.path.dirname(__file__)
            tiedostonimi = tiedostopolku +"/"+ tiedostonimi + ".txt"
            with open(tiedostonimi, "w", encoding="utf-8")as file:
                file.write(f"Kierros {kierros}\n\n")
                with redirect_stdout(file):
                    pelitilanne(pel, com, pel_laivat, com_laivat)
                print(f"Peli tallennettu tiedostoon {tiedostonimi}")
                break
        except PermissionError:
            print(f"Ei käyttöoikeuksia kansioon {tiedostopolku}")
        except Exception as e:
            print(f"Jokin meni pieleen tallennuksessa. Error: {e}")

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
    pelin päätyttyä tuloste muuttuu lopputuloksen mukaan sekä tallentaa pelin pelaajan halun mukaan pelaajan nimeämään tiedostoon
    """
    clear_console()
    kierros = 1
    pelaajan_pelilauta = luo_pelilauta()
    tietokoneen_pelilauta = luo_pelilauta()
    saannot()
    clear_console()
    tietokoneen_laivojen_sijainti(tietokoneen_pelilauta)
    keraa_laivojen_sijainnit(pelaajan_pelilauta)
    while True:
        com_laivojen_maara = laivojen_maara(tietokoneen_pelilauta)
        pel_laivojen_maara = laivojen_maara(pelaajan_pelilauta)
        print(f"Kierros {kierros}\n")
        print("Selite:\n  ~ = Tyhjä/Tuntematon\n  L = Laiva\n  O = Osuma\n  X = Ammus meni ohi\n")
        pelitilanne(pelaajan_pelilauta, tietokoneen_pelilauta, pel_laivojen_maara, com_laivojen_maara)
        if com_laivojen_maara == 0 or pel_laivojen_maara == 0:
            if com_laivojen_maara == 0 and pel_laivojen_maara == 0:
                print("Tasapeli! Olipas tasainen peli!")
            elif com_laivojen_maara == 0:
                print(f"Onnittelut! Voitit pelin! Sinulle jäi vielä {pel_laivojen_maara} laiva(a)!")
            else:
                print(f"Hävisit pelin! Parempi onni ensi kerralla. Vastustajalle jäi vielä {com_laivojen_maara} laiva(a).")
            while True:
                tallennus = input("Haluatko tallentaa pelin lopputuloksen? [y/n] ").lower()
                if tallennus == "y":
                    pelin_tallennus(kierros, pelaajan_pelilauta, tietokoneen_pelilauta, pel_laivojen_maara, com_laivojen_maara)
                    break
                elif tallennus == "n":
                    break
                else:
                    print("Virheellinen syöte. Syötä 'y' (kyllä) tai 'n' (ei).")
            break
        else:
            kierros += 1
            kysy_ampumakohde(tietokoneen_pelilauta)
            tietokoneen_ampumakohde(pelaajan_pelilauta)

if __name__ == "__main__":
    main()