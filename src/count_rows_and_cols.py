import sys
import numpy

from io import read_word_vecs, print_word_vecs
from io import read_ppdb

def read_doc(path):
	with open(path) as f:
		lines = f.read().splitlines();
	return lines

def save_to_file(lines, numRows, numCols, path):
	f = open(path, 'w');
	f.write('' + `numRows` + ' ' + `numCols` + '\n')
	for l in lines:
		l = l.split(" ")
		#fence post!
		f.write(l[0]);
		for token in l[1:len(l)]:
			if token is not " " and token is not "":
				f.write(' ' + token)
		f.write("\n")
	f.close()

def count_cols(lines):
	l = lines[0];
	counter = 0;
	for token in l.split(" "):
		if (token is not " " and token is not ""):
			counter = counter + 1;
	return counter;

if __name__=='__main__':
	print 'reading in word vectors from ' + sys.argv[1] + '...'
	lines = read_doc(sys.argv[1]);
	print 'done!'
	numRows = len(lines);
	numCols = count_cols(lines) - 1
	print 'number of columns: ' + `numCols`
	print 'writing out to ' + sys.argv[2] + '...'
	save_to_file(lines, numRows, numCols, sys.argv[2]);
	print 'done!'

