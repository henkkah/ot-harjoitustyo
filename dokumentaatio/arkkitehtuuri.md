# Arkkitehtuuri

## Rakenne

Ohjelman rakenne koostuu neljästä moduulista seuraavasti:  
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.PNG" width="150">  
- Ohjelma käynnistetään start.py moduulista.
- Ohjelmalla on tekstikäyttöliittymä (tui.py).
- Ohjelman sovelluslogiikka on koodattu logic.py moduuliin.
- Ohjelman data on pysyväistallennettu tietokantaan, jota käsitellään db.py moduulissa.

## Käyttöliittymä

Ohjelmassa on kaksi käyttöliittymänäkymää, kirjautumisnäkymä sekä budjettinäkymä:
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.PNG" width="500"> 
- Kirjautumisnäkymässä käyttäjä kirjautuu sovellukseen käyttäjätunnuksellaan sekä salasanallaan.
- Budjettinäkymässään käyttäjä näkee luomansa budjetin.

## Sovelluslogiikka

- Kirjautumisnäkymässä käyttäjä voi kirjautua sovellukseen käyttäjätunnuksellaan sekä salasanallaan. Mikäli käyttäjätunnusta ei ole, sen voi luoda näkymässä.
- Budjettinäkymässä näkee luomansa budjetin. Samassa näkymässä voi lisätä uusia budjettirivejä, muokata olemassaolevia rivejä sekä poistaa budjettirivejä.

## Tietojen pysyväistallennus

- Sovellus tallentaa tiedot pysyvästi tietokantaan.
- Moduuli db.py käsittelee tuota tietokantaa.

## Päätoiminnallisuudet

- Uuden budjettirivin lisääminen:
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/adding_new_budget_row.PNG" width="750">  
