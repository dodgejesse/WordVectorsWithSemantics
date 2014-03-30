import sys

from io import read_word_vecs
from ranking import spearmans_rho
from ranking import assign_ranks
from numpy.linalg import norm
from random import shuffle
from operator import itemgetter

''' Calculates the cosime sim between two numpy arrays '''
def cosine_sim(vec1, vec2):
	return vec1.dot(vec2)/(norm(vec1)*norm(vec2))
  
if __name__=='__main__':
	wordVectorFile = sys.argv[1]
	DIR = sys.argv[2]
	wordVectors = read_word_vecs(wordVectorFile)
	print '================================================================================='
	print "%6s" %"Serial", "%20s" % "Dataset", "%15s" % "Num Quests", "%15s" % "Not found", "%15s" % "%"
	print '================================================================================='
	FILES = ['EN-ESL-50.txt','EN-RD-300.txt', 'EN-TOEFL-80.txt']
	
	for i, FILE in enumerate(FILES):
		targets = []
		mostSim = []
		candidates = []
		for l in open(DIR+FILE,'r'):
			w = [c.strip() for c in l.strip().split('|')]
			targets.append(w[0])
			mostSim.append(w[1])
			shuffle(w[1:])
			candidates.append(w[1:])
		
		notFound, totalSize, correctCount = (0.0, 0.0, 0.0)
		for target,correct,candidateList in zip(targets,mostSim,candidates):
			if target not in wordVectors:
				notFound += 1.0
				continue
			qSims = []
			for candidate in candidateList:
				if candidate not in wordVectors:
					qSims = []
					notFound += 1.0
					break
				qSims.append((candidate,cosine_sim(wordVectors[target], wordVectors[candidate])))
			
			if qSims:
				totalSize += 1.0
				qSims = sorted(qSims,key=itemgetter(1),reverse=True)
				if qSims[0][0] == correct:
					correctCount += 1.0
		
		acc = 100*(correctCount/totalSize)
		print "%6s" % str(i+1), "%20s" % FILE, "%15s" % str(totalSize), "%15s" % str(notFound), "%15.4f" % acc