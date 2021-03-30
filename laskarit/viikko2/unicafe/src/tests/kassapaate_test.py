import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapäätteen_rahamäärä_ja_lounaiden_määrä_on_oikea(self):
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 0")

    # Edulliset käteisellä

    def test_käteisostolla_edullisen_maksu_riittävä_saldo_oikein_ja_lounaita_lisää(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(str(self.kassapaate), "saldo: 1002.4; edullisia: 1; maukkaita: 0")
    
    def test_käteisostolla_edullisen_maksu_riittävä_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
    
    def test_käteisostolla_edullisen_maksu_ei_riittävä_saldo_ei_muutu_ja_lounaita_ei_lisää(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 0")
    
    def test_käteisostolla_edullisen_maksu_ei_riittävä_maksu_vaihtorahana(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
    
    # Maukkaat käteisellä
    
    def test_käteisostolla_maukkaan_maksu_riittävä_saldo_oikein_ja_lounaita_lisää(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(str(self.kassapaate), "saldo: 1004.0; edullisia: 0; maukkaita: 1")
    
    def test_käteisostolla_maukkaan_maksu_riittävä_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_käteisostolla_maukkaan_maksu_ei_riittävä_saldo_ei_muutu_ja_lounaita_ei_lisää(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 0")
    
    def test_käteisostolla_maukkaan_maksu_ei_riittävä_maksu_vaihtorahana(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
    
    # Edulliset kortilla
    
    def test_korttiostolla_edullisen_maksu_riittävä_summa_veloitettu_kortilta(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 7.6")
    
    def test_korttiostolla_edullisen_maksu_riittävä_metodi_palauttaa_true(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)
    
    def test_korttiostolla_edullisen_maksu_riittävä_lounaita_lisää(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 1; maukkaita: 0")
    
    def test_korttiostolla_edullisen_maksu_ei_riittävä_summa_ei_veloitettu_kortilta(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 2.0")
    
    def test_korttiostolla_edullisen_maksu_ei_riittävä_metodi_palauttaa_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
    
    def test_korttiostolla_edullisen_maksu_ei_riittävä_lounaita_ei_lisää(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 0")
    
    # Maukkaat kortilla
    
    def test_korttiostolla_maukkaan_maksu_riittävä_summa_veloitettu_kortilta(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 6.0")
    
    def test_korttiostolla_maukkaan_maksu_riittävä_metodi_palauttaa_true(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
    
    def test_korttiostolla_maukkaan_maksu_riittävä_lounaita_lisää(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 1")
    
    def test_korttiostolla_maukkaan_maksu_ei_riittävä_summa_ei_veloitettu_kortilta(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 2.0")
    
    def test_korttiostolla_maukkaan_maksu_ei_riittävä_metodi_palauttaa_false(self):
        maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
    
    def test_korttiostolla_maukkaan_maksu_ei_riittävä_lounaita_ei_lisää(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 0")
    
    # Rahaa kortille ja kassaan
    
    def test_rahaa_kortille_kortin_saldo_kasvaa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        self.assertEqual(str(maksukortti), "saldo: 5.0")
    
    def test_rahaa_kortille_kassan_saldo_kasvaa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        self.assertEqual(str(self.kassapaate), "saldo: 1005.0; edullisia: 0; maukkaita: 0")
    
    def test_rahaa_kortille_negatiivinen_summa_argumenttina(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -500)
        self.assertEqual(str(maksukortti), "saldo: 0.0")
        self.assertEqual(str(self.kassapaate), "saldo: 1000.0; edullisia: 0; maukkaita: 0")
    