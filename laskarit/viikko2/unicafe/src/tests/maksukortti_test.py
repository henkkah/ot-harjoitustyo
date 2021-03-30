import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")
    
    def test_saldo_vähenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_metodi_ota_rahaa_palauttaa_true_jos_rahat_riittävät(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_metodi_ota_rahaa_palauttaa_false_jos_rahat_eivät_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
    