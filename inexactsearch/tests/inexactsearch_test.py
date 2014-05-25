#! /usr/bin/python
# -*- coding: utf-8 -*-
#run python -m chardetails.tests.chardetails_test from root directory
#of the repository
import unittest
from inexactsearch import getInstance


class TestInexactSearch(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_info(self):
        self.assertIsInstance(self.instance.get_info(), str)

    def test_bigram_average(self):
        self.assertLess(self.instance.bigram_average(u"toxicity", u"city"), 1)

    def test_compare(self):
        self.assertLess(self.instance.compare(u"toxicity", u"city"), 1)

    def test_search(self):
        self.assertLess(0, self.instance.search(u"സ്‌കൂള്‍ യുവജനോത്സവ \
        മത്സരങ്ങളില്‍ ഏറെ ശ്രദ്ധപിടിച്ചുപറ്റുന്ന  ഇനങ്ങളില്‍ ഒന്നാണ് ഏകാഭിനയം.\
        ഒന്നില്‍  കൂടുതല്‍", u"ഇനങ്ങളില്‍")[u"ഇനങ്ങളില്‍"])


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInexactSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
