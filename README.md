# Laivanupotus
12.12.2024  
Akseli Tervo  
Ohjelmoinnin perusteet -kurssin harjoitustyö  

## Tehtävänanto tiivistetysti
Konsolipohjainen python ohjelma, joka on pieni ja napakka.  
Koodissa käytetään kattavasti ja oikeaoppisesti opintojaksolla läpikäytyjä asioita.  
Koodin tulee olla kommentoitua, luettavaa ja johdonmukaista.  

## Käytännön toteutus:  
### Sovelluksen toiminta  
Sovelluksen funktiot:  
- luo_pelilauta: Luo pelilaudan, joka koostuu sisäkkäisistä sanakirjoista. Niiden arvoja kutsumalla ja muuttamalla muutetaan pelissä pelilautaa.  
- tietokoneen_laivojen_sijainti: Parametrinä annetaan tietokoneen pelilauta, palauttaa pelilaudan, johon sijoitettu laivat. Funktio arpoo ja sijoittaa tietokoneen 5 laivaa pelikentälle. Funktio tarkistaa arpoessa koordinaatteja, ettei sijainti ole jo varattu.  
- keraa_laivojen_sijainti: Parametrinä annetaan pelaajan pelilauta, palauttaa pelilaudan, johon sijoitettu pelaajan laivat. Funktio pyytää pelaajaa sijoittamaan laivat, kunnes 5 laivaa on sijoitettu onnistuneesti. Käyttää tulosta_pelilauta ja clear_console -funktioita näyttämään laivojen sijoitusvaiheen pelilaudan oikein käyttäjälle. Lisäksi käyttää tarkista_syote funktiota käyttäjän antaman koordinaatin tarkistamiseen.  
- tarkista_syote: Parametrinä annetaan pelaajan antama syöte, palauttaa tarkistustuloksen merkkijonona. Funktio tarkistaa käyttäjän antamat syötteet: niiden pituuden, tietotyypit ja että ne ovat pelikentän koordinaatistossa.  
- laivojen_maara: Parametrinä annetaan pelilauta, palauttaa laivojen määrän kokonaislukuna. Käy läpi parametrina annetun pelilaudan laskien jokaisen laivan eli sanakirjan arvon 'L'.  
- pelitilanne: Parametreinä annetaan pelaajan ja tietokoneen pelilaudat sekä molempien laivojen määrä. Funktio tulostaa pelin tilanteen halutulla tavalla konsoliin käyttäen tulosta_pelilauta funktiota. Lisäksi luo 'deepcopyn' copy-moduulilla tietokoneen pelilaudasta, jotta laivat voi piilottaa pelaajalta näkyvistä muokkaamatta alkuperäistä tietokoneen pelilautaa.  
- tulosta_pelilauta: Parametrinä annetaan pelilauta. Tulostaa halutun näköisen pelikentän, joka on helposti tulkittavissa.  
- kysy_ampumakohde: Parametrinä annetaan tietokoneen pelilauta, johon pelaaja ampuu. Palauttaa tietokoneen pelilaudan, johon pelaaja ampunut. Toimii keraa_laivojen_sijainnit funktion tavoin: pyytää syötteen, tarkistaa sen käyttämällä tarkista_syöte funktiota, ilmoittaa lisäksi osumat ja ohilaukaukset. Lisäksi käyttää clear_console funktiota tyhjentämään terminaalin, jotta ohilaukaus- ja osumaviestit pelaajalle tulevat seuraavalle kierrokselle näkyviin.   
- tietokoneen_laivojen_sijainti: Parametrina annetaan pelaajan pelilauta, johon tietokone ampuu. Palauttaa pelilaudan ampumisen jälkeen. Tulostaa pelaajalle ilmoitukset tietokoneen osumista ja ohilaukauksista.  
- pelin_tallennus: Parametreinä annetaan pelitilanne funktion vaatimat parametrit. Pyytää käyttäjää antamaan halutunlaisen tiedostonimen ja sopivan tiedostonimen saatuaan kirjoittaa tiedostoon aluksi viimeisen kierroksen numeron. Tämän jälkeen käyttää redirect_stdout 'context manageria' ohjaamaan kutsumansa pelitilanne funktion tulosteen tiedostoon. redirect_stdoutia käytetään, koska pelitilanne() ei palauta mitään. Funktio käyttää utf-8 encodingia, jotta ääkköset ja erikoismerkit tallentuu tiedostoon halutulla tavalla.  
- main: Pääohjelma käyttää edellä mainittuja funktioita pelin sujuvaan etenemiseen. Ennen pääsilmukkaa suoritettavat tapahtumat suoritetaan vain kerran ja silmukkaa suoritetaan niin kauan, kunnes jommalta kummalta tai molemmilta loppuu laivat. Pelin päätyttyä ilmoittaa lopputuloksen ja kysyy haluaako pelaaja tallentaa pelin lopputuloksen tiedostoon.  

### Muuta  
Ohjelmaan importattu moduulit: 'randint' tietokoneen arpomisen suorittamiseen, 'copy' deepcopyn tekemiseen, 'os' käyttöjärjestelmän tarkistukseen clear_console funktiossa ja oikeanlaisen tiedostopolun luomiseen eri käyttöjärjestelmillä sekä 'redirect_stdout' tietokoneen pelilaudan kopioimiseen.  
Käytin aikaa ohjelman tekemiseen noin 15-20 tuntia.  
Ohjelmassa käytetty kaikkia kurssin aiheita, paitsi luokkia.