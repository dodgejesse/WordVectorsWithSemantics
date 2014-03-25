import sys
import math
import numpy
import re

''' Normalize words to control the size of vocabulary '''
isNumber = re.compile(r'\d+.*')
def norm_word(word):
  if isNumber.search(word.lower()): 
    return '---num---'
  elif re.sub(r'\W+', '', word) == '': 
    return '---punc---'
  else: 
    return word.lower()

''' Read all the word vectors and normalize them '''
def read_word_vecs(filename):
  wordVectors = {}
  fileObject = open(filename, 'r')
  
  for lineNum, line in enumerate(fileObject):
    line = line.strip().lower()
    word = line.split()[0]
    wordVectors[word] = numpy.zeros(len(line.split())-1, dtype=float)
    for index, vecVal in enumerate(line.split()[1:]):
      wordVectors[word][index] = float(vecVal)
    ''' normalize weight vector '''
    wordVectors[word] /= math.sqrt((wordVectors[word]**2).sum() + 1e-6)
    
  sys.stderr.write("Vectors read from: "+filename+" \n")
  return wordVectors
  
def print_word_vecs(wordVectors, outFileName):
  sys.stderr.write('\nWriting down the vectors in '+outFileName+'\n')
  outFile = open(outFileName, 'w')  
  for word, values in wordVectors.iteritems():
    outFile.write(word+' ')
    for val in wordVectors[word]:
      outFile.write('%.4f' %(val)+' ')
    outFile.write('\n')      
  outFile.close()
  
''' Read the PPDB word relations as a dictionary '''
def read_ppdb(filename, wordVecs):
  ppDict = {}
  for line in open(filename, 'r'):
    words = line.lower().strip().split()
    ppDict[norm_word(words[0])] = [norm_word(word) for word in words[1:]]
  return ppDict