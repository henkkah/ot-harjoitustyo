## Testausdokumentti
Ohjelmaa on testattu sekä automatisoidusti Pythonin unittest-testauksella sekä manuaalisesti ohjelmaa monipuolisesti suorittamalla.  
Ohjelmasta ei ole löytynyt bugeja.  

# Sovelluslogiikka
application_test.py tiedostossa on sovelluslogiikan testit, joka testaa logic.py sekä db.py tiedostojen metodeita.  

# Testauskattavuus
Sovelluksen automatisoitu testauskattavuus on 48%.  
logic.py on testattu tärkeimpien toimintojen osalta.  
db.py:sta ei ole testattu kaikkea, sillä moni toiminto on yksinkertainen tietokantakysely.  
Ohjelmaa ajamalla on huomattu että tietokantakomennot toimivat oikein.  
<img src="https://github.com/henkkah/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/testauskattavuus.PNG" width="750">  

# Järjestelmätestaus
Sovelluksen järjestelmätestaus on tehty manuaalisesti.  
Sovellus toimii hyvin, siitä ei ole löytynyt bugeja - sovellus toimii niin kuin pitääkin.  
