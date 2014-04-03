import sys
import numpy

from io import read_word_vecs, print_word_vecs
from io import read_ppdb
from copy import deepcopy

def euclidean(wordVecs, ppDict, numIters):
	newWordVecs = deepcopy(wordVecs)
	wvVocab = set(newWordVecs.keys())
	loopVocab = wvVocab.intersection(set(ppDict.keys()))
	for it in range(numIters):
		#loop through every node also in ontology (otherwise just use data estimate)
		for word in loopVocab:
			wordNeighbours = set(ppDict[word]).intersection(wvVocab)
			numNeighbours = len(wordNeighbours)
			#no neighbours, pass - use data estimate
			if numNeighbours == 0:
				continue
			#NOTE: why such a high weight for data estimate?
			newVec = numNeighbours * wordVecs[word]
			#loop over neighbours and add to new vector (currently with weight 1)
			for ppWord in wordNeighbours:
				newVec += newWordVecs[ppWord]
			newWordVecs[word] = newVec/(2*numNeighbours)
	return newWordVecs
  
if __name__=='__main__':
	wordVecs = read_word_vecs(sys.argv[1])
	ppDict = read_ppdb(sys.argv[2], wordVecs)
	numIter = int(sys.argv[3])
	outFileName = sys.argv[4]
	
	''' Enrich the word vectors using ppdb and print the enriched vectors '''
	print_word_vecs(euclidean(wordVecs, ppDict, numIter), outFileName)
	