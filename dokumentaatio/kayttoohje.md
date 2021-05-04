# Käyttöohje

## Ohjelman käynnistäminen

Ohjelma käynnistetään komennolla:

```
poetry run invoke start
```

## Kirjautuminen

- Olemassaoleva käyttäjä kirjautuu sovellukseen komennolla 1. Kirjautumaan pääsee mikäli antaa oikean salasanan.
- Uusi käyttäjä voi luoda uuden käyttäjätunnuksen ja salasanan komennolla 2.

## Uuden budjettirivin lisääminen

- Budjettinäkymässä voi lisätä uuden budjettirivin komennolla 1.
- Tietona annetaan kategoria (Tulot/Menot/Varat/Velat), budjettirivin nimi sekä budjettisumma.

## Olemassaolevan budjettirivin muokkaaminen

- Budjettinäkymässä voi muokata olemassaolevaa budjettiriviä komennolla 2.
- Tietona annetaan muokattavan budjettirivin id sekä uusi summa.

## Olemassaolevan budjettirivin poistaminen

- Budjettinäkymässä voi poistaa olemassaolevan budjettirivin komennolla 3.
- Tietona annetaan poistettavan budjettirivin id.
