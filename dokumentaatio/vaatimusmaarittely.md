# Vaatimusmäärittely

## Sovelluksen nimi
Budjetointisovellus

## Sovelluksen tarkoitus
Sovelluksen käyttäjä voi budjetoida henkilökohtaisen taloutensa tulot ja menot sekä varat ja velat.  
Sovellukseen kirjaudutaan, minkä ansiosta eri käyttäjillä on omat budjettinsa.

## Käyttäjät
Sovellusta käyttävät "normaalikäyttäjät".  
Lisäksi sovelluksessa on "pääkäyttäjä"-rooli, jota järjestelmän ylläpitäjä käyttää tarvittaessa.

## Käyttöliittymäluonnos
Aluksi sovellukseen kirjaudutaan käyttäjätunnuksella.  
Kirjauduttuaan käyttäjä näkee näkymän luomastaan budjetista.  
Alhaalla on nappi, josta pääsee lisäämään tai poistamaan budjettirivejä, tai muokkaamaan olemassaolevia rivejä.  
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kayttoliittymaluonnos.PNG" width="500">

## Sovelluksen toiminnallisuus
### Alkunäkymä
- Käyttäjätunnuksen luominen
    - Jos käyttäjällä ei ole vielä tunnusta - tehty
    - Käyttäjätunnukseksi ei voi valita olemassaolevaa tunnusta - tehty
- Sovellukseen kirjautuminen
    - Käyttäjätunnuksella sekä salasanalla - tehty
### Päänäkymä
- Käyttäjä näkee näkymän budjetoimistaan tuloista ja menoista, sekä varoista ja veloista. - tehty
- Lisäksi näkyy yhteenveto- ja tilastotietoa. - tehty
- Alhaalla on nappeja, josta pääsee lisäämään tai poistamaan budjettirivejä. - tehty
- Mahdollisuus olemassaolevien rivien muokkaamiseen. - tehty
- Sovelluksesta pääsee kirjautumaan ulos. - tehty

## Jatkokehitysideoita
Mikäli aikaa riittää, sovellusta kehitetään esim:
- Toteumien tuominen sovellukseen (toteutuneet tulot ja menot, varat ja velat)
    - Käyttäjä syöttää tiedoston sovellukseen (pitää olla tietyssä formaatissa, joka ohjeistettu)
    - Tällöin päänäkymässä näkyy sekä budjetit että toteumat, jonka avulla käyttäjä voi tehdä analyysia sekä adjustoida budjettejaan
- Budjettirivien yhteyteen kommentointiominaisuus, eli tiettyä budjettiriviä voisi kommentoida
- Toiminnallisuus useamman budjetin luomiseen per käyttäjä
