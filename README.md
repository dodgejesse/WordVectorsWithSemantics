Enriching Word Vectors Using Lexical Semantics Resources
--------------------------------------------------------

1. To enrich using PPDB:-

   <code>python src/enrich.py orig-vector-file corpora/clean-1.0-xl-lexical.txt 10 out-vector-file</code>
   10 is the number of iterations here, usually 5 also gives the same results.

2. To evaluate on WordSim:-

   <code>python src/all-wordsim.py vector-file corpora/ </code>
