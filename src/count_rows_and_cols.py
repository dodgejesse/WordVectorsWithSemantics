import sys
import numpy

from io import read_word_vecs, print_word_vecs
from io import read_ppdb

def read_doc(path):
	with open(path) as f:
		lines = f.read().splitlines();
	return lines

def save_to_file(lines, numRows, numCols, path, enriched):
	f = open(path, 'w');
	if enriched == 'enriched':
		numCols = numCols - 1;
	f.write('' + `numRows` + ' ' + `numCols` + '\n')
	for l in lines:
		l = l.split(" ")
		#the enriched files have a similar 
		if enriched == "enriched":
			l = l[0:len(l)-1]
		#fence post!
		f.write(l[0]);
		for token in l[1:len(l)]:
			f.write(' ' + token)
		f.write("\n")
	f.close()


if __name__=='__main__':
	print 'reading in word vectors from ' + sys.argv[1] + '...'
	lines = read_doc(sys.argv[1]);
	print 'done!'
	numRows = len(lines);
	numCols = len(lines[1].split(' ')) - 1
	print 'writing out to ' + sys.argv[2] + '...'
	save_to_file(lines, numRows, numCols, sys.argv[2], sys.argv[3]);
	print 'done!'

