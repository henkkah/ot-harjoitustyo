# Arkkitehtuuri

## Rakenne

Ohjelman rakenne koostuu neljästä moduulista seuraavasti:  
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri.PNG" width="150">  
- Ohjelma käynnistetään start.py moduulista.
- Ohjelmalla on graafinen käyttöliittymä (gui.py).
- Ohjelman sovelluslogiikka on koodattu logic.py moduuliin.
- Ohjelman data on pysyväistallennettu tietokantaan, jota käsitellään db.py moduulissa.

## Käyttöliittymä

Ohjelmassa on kaksi käyttöliittymänäkymää, kirjautumisnäkymä sekä budjettinäkymä:
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoliittymaluonnos.PNG" width="500">  
- Kirjautumisnäkymässä käyttäjä kirjautuu sovellukseen käyttäjätunnuksellaan sekä salasanallaan.
- Budjettinäkymässään käyttäjä näkee luomansa budjetin, sekä pystyy lisäämään ja poistamaan rivejä.

## Sovelluslogiikka

- Kirjautumisnäkymässä käyttäjä voi kirjautua sovellukseen käyttäjätunnuksellaan sekä salasanallaan. Mikäli käyttäjätunnusta ei ole, sen voi luoda näkymässä.
- Budjettinäkymässä näkee luomansa budjetin. Samassa näkymässä voi lisätä uusia budjettirivejä sekä poistaa budjettirivejä.

## Tietojen pysyväistallennus

- Sovellus tallentaa tiedot pysyvästi tietokantaan.
- Moduuli db.py käsittelee tuota tietokantaa.

## Päätoiminnallisuudet

- Uuden budjettirivin lisääminen:
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/adding_new_budget_row.PNG" width="750">  
- Olemassaolevan budjettirivin poistaminen:
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/deleting_existing_budget_row.PNG" width="750">  
