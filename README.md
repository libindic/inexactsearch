# LibIndic Inexact Search


[![Build Status](https://travis-ci.org/libindic/inexactsearch.svg?branch=master)](https://travis-ci.org/libindic/indicinexactsearch)
[![Coverage Status](https://coveralls.io/repos/github/libindic/inexactsearch/badge.svg?branch=master)](https://coveralls.io/github/libindic/indicinexactsearch?branch=master)


LibIndic's inexactsearch module is a [Fuzzy string search](http://en.wikipedia.org/wiki/Fuzzy_string_searching). This application illustrates the combined use of [Edit distance](http://en.wikipedia.org/wiki/Levenshtein_distance) and [Indic Soundex](http://silpa.org.in/Soundex) algorithm.

By mixing both written like(edit distance) and sounds like(soundex), we achieve an efficient aproximate string searching. This application is capable of cross language string search too. That means, you can search Hindi words in Malayalam text. If there is any Malayalam word, which is approximate transliteration of hindi word, or sounds alike the hindi words, it will be returned as an approximate match. The "written like" algorithm used here is a bigram average algorithm.  The ratio of common bigrams in two strings and average number of bigrams will give a factor which is greater than zero and less than 1. Similarly the soundex algorithm also gives a weight. By selecting words which has comparison weight more than the threshold weight(which 0.6), we get the search results.

## Installation
1. Clone the repository `git clone https://github.com/libindic/inexactsearch.git`
2. Change to the cloned directory `cd inexactsearch`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/inexactsearch*.tar.gz`

## Usage
```
>>> from libindic.inexactsearch import InexactSearch
>>> instance = InexactSearch()
>>> result = instance.search(u"कालडी केरल के एर्नाकुलम जिले में पेरियार नदी के पूर्व में स्थित एक गाँव है", u"കാലടി")
>>> matches = [word for word, similarity in result.items() if similarity > 0.8]
>>> for match in matches:
...     print(match)
...
कालडी
```

For more details read the [docs](http://inexactsearch.rtfd.org/)
