#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Approximate Search
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com


_all_ = ['InexactSearch', 'getInstance']

import os
import soundex


class InexactSearch:
    """
    This class provides methods for fuzzy searching using word distance
    as well as phonetics.
    """
    def bigram_average(self,str1, str2):
        """Return approximate string comparator measure (between 0.0 and 1.0)
        using bigrams.
        :param str1: string 1 for comparison
        :str1 type : str
        :param str2: string 2 for comparison
        :str2 type : str
        :returns: int score between 0.0 and 1.0

        >>> score = bigram_avearage(str1, str2)
        0.7


        Bigrams are two-character sub-strings contained in a string. For example,
        'peter' contains the bigrams: pe,et,te,er.

        This routine counts the number of common bigrams and divides by the
        average number of bigrams. The resulting number is returned.
        """

        # Quick check if the strings are the same - - - - - - - - - - - - - - - - - -
        #
        if (str1 == str2):
            return 1
        bigr1 = []
        bigr2 = []
        # Make a list of bigrams for both strings - - - - - - - - - - - - - - - - - -
        #
        for i in range(1, len(str1)):
            bigr1.append(str1[i-1:i+1])
        for i in range(1, len(str2)):
            bigr2.append(str2[i-1:i+1])

        # Compute average number of bigrams - - - - - - - - - - - - - - - - - - - - -
        #
        average = (len(bigr1)+len(bigr2)) / 2.0
        if (average == 0.0):
            return str1

        # Get common bigrams  - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #
        common = 0.0

        if (len(bigr1) < len(bigr2)):  # Count using the shorter bigram list
            short_bigr = bigr1
            long_bigr = bigr2
        else:
            short_bigr = bigr2
            long_bigr = bigr1

        for b in short_bigr:
            if (b in long_bigr):
                if long_bigr.index(b) == short_bigr.index(b) :
                    common += 1.0
                else:
                    dislocation = (long_bigr.index(b) -
                                   short_bigr.index(b)) / average
                    if dislocation < 0 :
                        dislocation = dislocation * -1
                    common += 1.0 - dislocation
                long_bigr[long_bigr.index(b)] = []  # Mark this bigram as counted

        w = common / average
        return w

    def compare(self, string1, string2):
        """
        Compare strings using soundex if not possible givees biggram avearage.

        :param str1: string 1 for comparison.
        :type str1: str.
        :param str2: string 2 for comparison
        :type str2: str.
        :returns: int score between 0.0 and 1.0

        """
        weight = 0
        if string1 == string2:
            return 1
        sx = soundex.getInstance()
        soundex_match = sx.compare(string1, string2)
        if soundex_match == 0:
            weight = 1.0
        if soundex_match == 1:
            weight = 0.9
        if soundex_match == 2:
            weight = 0.8
        if weight == 0:
            return self.bigram_average(string1, string2)
        else:
            return weight

    def search(self, text, key):
        """
        Searches for the key in the given text.

        :param text: text in which search has to be done.
        :type text: str.
        :param key: key which  has  to be searched
        :type key: str.
        :returns: array of strings -> search results

         >>> a.search(u"അത് പരീക്ഷിച്ചുനോക്കുന്നതിന്, ചുവടെ നിങ്ങളുടെ ഭാഷയും എഴുത്ത് ഉപകരണങ്ങളും തിരഞ്ഞെടുത്ത് ടൈപ്പുചെയ്യാൻ ആരംഭിക്കുക.",u"ചുവടെ")
         u'\u0d05\u0d24\u0d4d': 0.0,
         u'\u0d06\u0d30\u0d02\u0d2d\u0d3f\u0d15\u0d4d\u0d15\u0d41\u0d15.': 0.0,
         u'\u0d09\u0d2a\u0d15\u0d30\u0d23\u0d19\u0d4d\u0d19\u0d33\u0d41\u0d02': 0.0,
         u'\u0d0e\u0d34\u0d41\u0d24\u0d4d\u0d24\u0d4d': 0.0,
         u'\u0d1a\u0d41\u0d35\u0d1f\u0d46': 1,
         u'\u0d1f\u0d48\u0d2a\u0d4d\u0d2a\u0d41\u0d1a\u0d46\u0d2f\u0d4d\u0d2f\u0d3e\u0d7b': 0.0,
         u'\u0d24\u0d3f\u0d30\u0d1e\u0d4d\u0d1e\u0d46\u0d1f\u0d41\u0d24\u0d4d\u0d24\u0d4d': 0.0,
         u'\u0d28\u0d3f\u0d19\u0d4d\u0d19\u0d33\u0d41\u0d1f\u0d46': 0.05555555555555556,
         u'\u0d2a\u0d30\u0d40\u0d15\u0d4d\u0d37\u0d3f\u0d1a\u0d4d\u0d1a\u0d41\u0d28\u0d4b
         \u0d15\u0d4d\u0d15\u0d41\u0d28\u0d4d\u0d28\u0d24\u0d3f\u0d28\u0d4d,': 0.02551020408163265,
         u'\u0d2d\u0d3e\u0d37\u0d2f\u0d41\u0d02': 0.0}

        """
        key = key.strip()
        words = text.split()
        search_results = {}
        for word in words:
            word = word.strip()
            search_results[word]= self.compare(word, key)
        return search_results

    def get_module_name(self):
        """ returns module name"""
        return "Approximate Search"

    def get_info(self):
        """ Returns info on the module"""
        return "Approximate Search for a string in the given text. Based on bigram search algorithm and indic soundex algorithms"

def getInstance():
    """
    returns an instance of :class: `InexactSearch` class.
    """
    return InexactSearch()
