Approximate String Search
=========================

This is a [Fuzzy string search](http://en.wikipedia.org/wiki/Fuzzy_string_searching)
application. This application illustrates the combined use of[ Edit distance](http://en.wikipedia.org/wiki/Levenshtein_distance)
and [Indic Soundex](http://silpa.org.in/Soundex) algorithm.

By mixing both written like(edit distance) and sounds like(soundex), 
we achieve an efficient aproximate string searching. This application
is capable of cross language string search too. That means, you can
search Hindi words in Malayalam text. If there is any Malayalam word, 
which is approximate transliteration of hindi word, or sounds alike 
the hindi words, it will be returned as an approximate match. The 
"written like" algorithm used here is a bigram average algorithm. 
The ratio of common bigrams in two strings and average number of bigrams
will give a factor which is greater than zero and less than 1. Similarly
the soundex algorithm also gives a weight. By selecting words which has
comparison weight more than the threshold weight(which 0.6), we get the 
search results. 

You can run tests by rubbing ` python setup.py test ` .At the moment very few
test cases are available.Feel free to contribute tests for your  language.

Read the [docs](http://inexactsearch.readthedocs.org/en/latest/) for more info 

**This module is not yet complete dependency modules are yet to be complete**
