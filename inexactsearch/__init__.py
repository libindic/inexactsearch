#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Approximate Search
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.


_all_ = ['InexactSearch', 'getInstance']

from silpa_common import servicemethod
import soundex


class InexactSearch(object):
    """
       This class provides methods for fuzzy searching using word
       distance as well as phonetics.
    """

    def __init__(self):
        self.sx = soundex.getInstance()

    def _countCommon(self, shrtBigr, lngBigr, average):
        common = 0.0
        for indexShrt, bigr in enumerate(shrtBigr):
            if bigr in lngBigr:
                indexLng = lngBigr.index(bigr)
                if indexLng == indexShrt:
                    common += 1.0
                else:
                    dislocation = (indexLng - indexShrt)/average
                    if dislocation < 0:
                        dislocation *= -1
                    common += 1.0 - dislocation

        return common

    def _createBigram(self, string):
        bigram = []
        for i in range(1, len(string)):
            bigram.append(string[i-1:i+1])

        return bigram

    def bigram_average(self, str1, str2):
        """Return approximate string comparator measure (between 0.0 and 1.0)
        using bigrams.

        :param str1: string 1 for comparison
        :str1 type : str
        :param str2: string 2 for comparison
        :str2 type : str
        :returns: int score between 0.0 and 1.0

        >>> score = bigram_avearage(str1, str2)
        0.7


        Bigrams are two-character sub-strings contained in a
        string. For example, 'peter' contains the bigrams:
        pe,et,te,er.

        This routine counts the number of common bigrams and divides
        by the average number of bigrams. The resulting number is
        returned.
        """

        if (str1 == str2):
            return 1

        bigr1 = self._createBigram(str1)
        bigr2 = self._createBigram(str2)

        average = (len(bigr1) + len(bigr2)) / 2.0

        common = 0.0

        if (len(bigr1) < len(bigr2)):  # Count using the shorter bigram list
            common = self._countCommon(bigr1, bigr2, average)
        else:
            common = self._countCommon(bigr2, bigr1, average)

        return common / average

    def compare(self, string1, string2):
        ''' Compare strings using soundex if not possible gives
        biggram avearage.

        :param str1: string 1 for comparison.
        :type str1: str.
        :param str2: string 2 for comparison
        :type str2: str.
        :returns: int score between 0.0 and 1.0

        '''
        weight = 0
        if string1 == string2:
            return 1.0

        soundex_match = self.sx.compare(string1, string2)

        if soundex_match == 1:
            weight = 0.9

        if soundex_match == 2:
            weight = 0.8

        if weight == 0:
            return self.bigram_average(string1, string2)
        else:
            return weight

    @servicemethod
    def search(self, text, key):
        '''Searches for the key in the given text. This function uses
        :method: `InexactSearch.compare` for doing approx search.

        :param text: text in which search has to be done.
        :type text: str.
        :param key: key which has to be searched
        :type key: str.
        :returns: A dictionary with words in the string as keys and
        the score against the key as the value
        '''
        key = key.strip()
        words = text.split()
        search_results = {}
        for word in words:
            word = word.strip()
            search_results[word] = self.compare(word, key)

        return search_results


def getInstance():
    '''This function returns instance of :py:class:`~InexactSearch`
    '''
    return InexactSearch()
