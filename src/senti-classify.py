import sklearn,sys
import numpy, math
import gzip

from sklearn.linear_model import LogisticRegression
from nltk.stem import WordNetLemmatizer 
from sklearn import svm
from nltk.corpus import stopwords
from nltk import word_tokenize 

lemmatizer = WordNetLemmatizer()
stopWords = stopwords.words('english')

''' Read all the word vectors and normalize them '''
def read_word_vecs(filename):
  wordVectors = {}
  if filename.endswith(".gz"): fileObject = gzip.open(filename, 'r')
  else: fileObject = open(filename, 'r')
  
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
    
def get_norm_words(sentence):
  return [lemmatizer.lemmatize(word) for word in word_tokenize(sentence)]
  
def train(x_train, y_train, C):
  clf = LogisticRegression(C=C)
  #clf = svm.SVC(C=0.01, kernel='linear')
  clf.fit(x_train, y_train)
  return clf
  
# obtain features for the training data
def read_and_featurize(filename, vocab, wordVecs):
  X, Y = ([], [])
  for line in open(filename, 'r'):
    category, sent = line.strip().lower().split(" ", 1)
    words = get_norm_words(sent)
    # count word frequency
    x_wordVec = numpy.zeros(len(wordVecs["the"]))
    x_words = numpy.zeros(len(vocab))
    for word in words:
      if word in vocab:
        x_words[vocab[word]] += 1
      if word in wordVecs:
        x_wordVec += wordVecs[word]
    x_wordVec /= len(words)
    x_words /= len(words)
    #X.append(numpy.concatenate((x_words, x_wordVec)))
    X.append(x_wordVec)
    Y.append(category)
    
  return X, Y
  
def get_acc(classifier, x, y):
  y_pred = classifier.predict(x)
  total, error = (0., 0.)
  for yi, yi_pred in zip(y, y_pred):
    if yi != yi_pred:
      error += 1
    total += 1
  return 100*(total-error)/total
  
def get_vocab(filename):
  vocab = {}
  wordIndex = 0
  for line in open(filename, 'r'):
    category, sent = line.strip().lower().split(" ", 1)
    words = get_norm_words(sent)
    for word in words:
      if word not in vocab and word not in stopWords:
        vocab[word] = wordIndex
        wordIndex += 1
  return vocab
  
if __name__ == "__main__":
  
  if len(sys.argv) < 4: 
    print "Usage: python senti-classify.py trFile devFile testFile"
    sys.exit(0)
    
  trFile, devFile, testFile, vecFile = (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
  vocab = get_vocab(trFile)
  wordVecs = read_word_vecs(vecFile)
  
  x_train, y_train = read_and_featurize(trFile, vocab, wordVecs)
  x_dev, y_dev = read_and_featurize(devFile, vocab, wordVecs)
  x_test, y_test = read_and_featurize(testFile, vocab, wordVecs)
  
  print "Train: ", len(y_train), "Dev: ", len(y_dev), "Test: ", len(y_test)
  for reg in [0.01, 0.1, 1, 10, 100, 1000]:
    classifier = train(x_train, y_train, reg)
    print "Reg =", reg, get_acc(classifier, x_dev, y_dev), get_acc(classifier, x_test, y_test)




