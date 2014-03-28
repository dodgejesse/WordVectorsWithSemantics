Enriching Word Vectors Using Lexical Semantics Resources
--------------------------------------------------------

1. To enrich using PPDB:-

   python src/enrich.py orig-vector-file corpora/clean-1.0-xl-lexical.txt 10 out-vector-file
   10 is the number of iterations here, usually 5 also gives the same results.

2. To evaluate on WordSim:-

   python src/all-wordsim.py vector-file corpora/
