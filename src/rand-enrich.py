import sys
import numpy
import random

from io import read_word_vecs, print_word_vecs
from io import read_ppdb
from copy import deepcopy

def euclidean(wordVecs, numIters):
	random.seed()
	newWordVecs = deepcopy(wordVecs)
	wvVocabID = newWordVecs.keys() 
	wvDict = {w:(random.randint(0,2),[wvVocabID[random.randint(0,len(wvVocabID)-1)] for i in range(random.randint(0,10))]) for w in newWordVecs}
	
	for it in range(numIters):
		#loop through every node also in ontology (otherwise just use data estimate)
		for word in wvDict:
			if (wvDict[word][0] == 0) or (len(wvDict[word][1]) == 0):
				continue
			numNeighbours = len(wvDict[word][1])
			#NOTE: why such a high weight for data estimate?
			newVec = numNeighbours * wordVecs[word]
			#loop over neighbours and add to new vector (currently with weight 1)
			for ppWord in wvDict[word][1]:
				newVec += newWordVecs[ppWord]
			newWordVecs[word] = newVec/(2*numNeighbours)
	return newWordVecs
  
if __name__=='__main__':
	wordVecs = read_word_vecs(sys.argv[1])
	numIter = int(sys.argv[2])
	outFileName = sys.argv[3]
	
	''' Enrich the word vectors using ppdb and print the enriched vectors '''
	print_word_vecs(euclidean(wordVecs, numIter), outFileName)
	