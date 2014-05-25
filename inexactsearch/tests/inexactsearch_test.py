# -*- coding: utf-8 -*-
import unittest
import soundex
from inexactsearch import getInstance


class InexactSearchTest(unittest.TestCase):

    def assertInexactSearchSuccess(self, result):
        filtered_keys = (key for value, key in
                         sorted(zip(result.values(), result.keys()))
                         if value > 0.8)
        self.assertGreater(len(list(filtered_keys)), 0)

    def setUp(self):
        self.ies = getInstance()
        self.sndx = soundex.getInstance()

    def test_bigram_average(self):
        self.assertAlmostEqual(self.ies.bigram_average(u"toxicity", u"city"),
                               0.12, places=2)
        self.assertEqual(self.ies.bigram_average(u"Mangalore", u"Bangalore"),
                         0.875)
        self.assertAlmostEqual(self.ies.bigram_average(u"Cauliflower",
                                                       u"Sunflower"), 0.432,
                               places=3)
        self.assertAlmostEqual(self.ies.bigram_average(u"apple", u"Pineapple"),
                               0.22, places=2)
        self.assertEqual(self.ies.bigram_average("mango", "mango"), 1)
        self.assertAlmostEqual(self.ies.bigram_average("apple", "planet"),
                               0.123, places=3)

    def test_compare(self):
        self.assertEqual(self.ies.compare("toxicity", "city"), 0.8)
        self.assertEqual(self.ies.compare(u"ಮಾವಿನ ಹಣ್ಣು", u"माविन हण्णु "),
                         0.9)
        self.assertEqual(self.ies.compare(u"ಮಾವಿನ ಹಣ್ಣು", "mango"), 0.0)
        self.assertEqual(self.ies.compare(u"ಮಾವಿನ ಹಣ್ಣು", u"ಮಾವಿನ ಹಣ್ಣು"), 1)

    def test_search(self):
        self.assertInexactSearchSuccess(self.ies.search(u"സ്‌കൂള്‍ യുവജനോത്സവ \
        മത്സരങ്ങളില്‍ ഏറെ ശ്രദ്ധപിടിച്ചുപറ്റുന്ന  ഇനങ്ങളില്‍ ഒന്നാണ് ഏകാഭിനയം.\
        ഒന്നില്‍  കൂടുതല്‍", u"ಒನ್ನಿಲ್"))
