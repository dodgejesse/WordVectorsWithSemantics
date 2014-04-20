import sys, os
from sets import Set
import numpy
import xml.etree.ElementTree as ET

#from io import read_word_vecs, print_word_vecs
#from io import read_ppdb

def read_lu_dir(lu_dir, frames_to_words):
	print 'reading from ' + lu_dir
	counter = 0;
	for fn in os.listdir(lu_dir):
		counter = counter + 1;
		if (counter % 100 == 0):
			print '.',
			sys.stdout.flush()
		if (counter % 10000 == 0):
			print '.'
			sys.stdout.flush()
		tree = ET.parse(lu_dir + '/' + fn);
		root = tree.getroot();
		lex = '';
		for l in root.findall('{http://framenet.icsi.berkeley.edu}lexeme'):
		 	lex = lex + ' ' + l.attrib['name'];
		lex = lex[1:];
		if ' ' in lex or 'frame' not in root.attrib:
			continue
		if '_' in lex:
			lex = lex.split('_')[0];
		if root.attrib['frame'] in frames_to_words:
			frames_to_words[root.attrib['frame']].add(lex);
		else:
			frames_to_words[root.attrib['frame']] = Set([lex]);
	

def read_frame_dir(frame_dir, frames_to_words):
	print 'reading from ' + frame_dir
	counter = 0;
	for fn in os.listdir(frame_dir):
		counter = counter + 1;
		if (counter % 100 == 0):
			print '.',
			sys.stdout.flush()
		if (counter % 10000 == 0):
			print '.'
			sys.stdout.flush()
		tree = ET.parse(frame_dir + '/' + fn);
		root = tree.getroot();
		for lexUnit in root.findall('{http://framenet.icsi.berkeley.edu}lexUnit'):
			lex = lexUnit.attrib['name'].split('.')[0];
			if ' ' in lex:
				continue
			if '_' in lex:
				if '(' in lex:
					lex = lex.split('_')[0]
				else:
					continue
			
			if root.attrib['name'] in frames_to_words:
				frames_to_words[root.attrib['name']].add(lex);
			else:
				frames_to_words[root.attrib['name']] = Set([lex]);

	counter = 0;
	for frame in frames_to_words:
		print frame, frames_to_words[frame]
		counter = counter + 1;
		if counter > 10:
			break


def print_frames_to_words(frames_to_words, out_loc):
	f = open(out_loc, 'w')
	for frame in frames_to_words:
		for word in frames_to_words[frame]:
			f.write(word);
			other_words = frames_to_words[frame] - Set([word]);
			for other_word in other_words:
				f.write (' ' + other_word);
			f.write('\n')
			


if __name__=='__main__':
	frames_to_words = {}
	lu_dir = sys.argv[1] + '/lu'
	frame_dir = sys.argv[1] + '/frame'
	fulltext_dir = sys.argv[1] + '/fulltext'
	read_lu_dir(lu_dir, frames_to_words)
	read_frame_dir(frame_dir, frames_to_words)
	print_frames_to_words(frames_to_words, sys.argv[2])




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
