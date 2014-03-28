import sys
import numpy

from io import read_word_vecs, print_word_vecs
from io import read_ppdb

def euclidean(wordVecs, ppDict, iter):
  
  for word in ppDict:
    if word in wordVecs:
      countPPWords = len([ppWord for ppWord in ppDict[word] if ppWord in wordVecs])
      newVec = countPPWords * wordVecs[word]
      for ppWord in ppDict[word]:
        if ppWord in wordVecs:
          newVec += wordVecs[ppWord]
          countPPWords += 1
      if countPPWords > 0:
      	newVec /= 2*countPPWords
      	wordVecs[word] = newVec  
  return wordVecs
  
if __name__=='__main__':
  
  wordVecs = read_word_vecs(sys.argv[1])
  ppDict = read_ppdb(sys.argv[2], wordVecs)
  numIter = int(sys.argv[3])
  outFileName = sys.argv[4]
  
  ''' Enrich the word vectors using ppdb '''
  newWordVecs = euclidean(wordVecs, ppDict, numIter)
  ''' Print the enriched vectors '''
  print_word_vecs(wordVecs, outFileName)
