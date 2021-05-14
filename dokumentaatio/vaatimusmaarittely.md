# Vaatimusmäärittely

## Sovelluksen nimi
Budjetointisovellus

## Sovelluksen tarkoitus
Sovelluksen käyttäjä voi budjetoida henkilökohtaisen taloutensa tulot ja menot sekä varat ja velat.  
Sovellukseen kirjaudutaan, minkä ansiosta eri käyttäjillä on omat budjettinsa.

## Käyttäjät
Sovellusta käyttävät "normaalikäyttäjät".  

## Käyttöliittymä
Aluksi sovellukseen kirjaudutaan käyttäjätunnuksella ja salasanalla.  
Kirjauduttuaan käyttäjä näkee näkymän luomastaan budjetista.  
Alhaalla on napit, joilla pääsee lisäämään tai poistamaan budjettirivejä.  
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoliittymaluonnos.PNG" width="500">

## Sovelluksen toiminnallisuus
### Alkunäkymä
- Käyttäjätunnuksen luominen
    - Jos käyttäjällä ei ole vielä tunnusta - tehty
    - Käyttäjätunnukseksi ei voi valita olemassaolevaa tunnusta - tehty
    - Salasanan voi valita vapaasti (tai jättää tyhjäksi) - tehty
- Sovellukseen kirjautuminen
    - Käyttäjätunnuksella sekä salasanalla (salasanan oikeellisuus tarkistetaan) - tehty
### Päänäkymä
- Käyttäjä näkee näkymän budjetoimistaan tuloista ja menoista, sekä varoista ja veloista. - tehty
- Lisäksi näkyy yhteenveto- ja tilastotietoa. - tehty
- Alhaalla on nappeja, josta pääsee lisäämään tai poistamaan budjettirivejä. - tehty
- Sovelluksesta pääsee kirjautumaan ulos. - tehty

## Jatkokehitysideoita
Mikäli aikaa riittää, sovellusta kehitetään esim:
- Olemassaolevien rivien muokkaustoiminto
- Toteumien tuominen sovellukseen (toteutuneet tulot ja menot, varat ja velat)
    - Käyttäjä syöttää tiedoston sovellukseen (pitää olla tietyssä formaatissa, joka ohjeistettu)
    - Tällöin päänäkymässä näkyy sekä budjetit että toteumat, jonka avulla käyttäjä voi tehdä analyysia sekä adjustoida budjettejaan
- Budjettirivien yhteyteen kommentointiominaisuus, eli tiettyä budjettiriviä voisi kommentoida
- Toiminnallisuus useamman budjetin luomiseen per käyttäjä
