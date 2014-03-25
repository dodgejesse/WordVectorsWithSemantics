import sys
import numpy

from io import read_word_vecs, print_word_vecs
from io import read_ppdb

def euclidean(wordVecs, ppDict, iter, alpha):
  
  for word in ppDict:
    if word in wordVecs:
      newVec = alpha * wordVecs[word]
      countPPWords = 0
      for ppWord in ppDict[word]:
        if ppWord in wordVecs:
          newVec += wordVecs[ppWord]
          countPPWords += 1
      newVec /= (alpha + countPPWords)
      wordVecs[word] = newVec  
  return wordVecs
  
if __name__=='__main__':
  
  wordVecs = read_word_vecs(sys.argv[1])
  ppDict = read_ppdb(sys.argv[2], wordVecs)
  numIter = int(sys.argv[3])
  
  ''' Enrich the word vectors using ppdb '''
  newWordVecs = euclidean(wordVecs, ppDict, numIter, 5)
  ''' Print the enriched vectors '''
  print_word_vecs(wordVecs, 'y.txt')