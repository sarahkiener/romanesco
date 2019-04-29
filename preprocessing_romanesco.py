#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# maschinelle Übersetzung
# Übung 4
# Autorin: Sarah Kiener
# Matrikelnr.: 09-110-958
# Datum: 24.04.2019

from nltk import tokenize



def long_text():
	outfilepath = './'
	with open('austen.txt', encoding='utf-8') as infile:
		for line in infile:
			if line == '\n':
				with open(outfilepath + 'austen_long_text.txt', 'a') as outfile:
					outfile.write(line)
			else:
				line = line.rstrip()
				with open(outfilepath + 'austen_long_text.txt', 'a') as outfile:
					outfile.write(line + ' ')



def sent_tokenize(input):
	sentences = tokenize.sent_tokenize(input)
	return sentences

def word_tokenize(input):
	words = tokenize.word_tokenize(input)
	return words

def sents():
	outfilepath = './'
	with open('austen_long_text.txt', encoding='utf-8') as infile:
		for line in infile:
			sents = sent_tokenize(line)
			for sent in sents:
				with open(outfilepath + 'austen_sents.txt', 'a') as outfile:
					outfile.write(sent + '\n')


def words():
	outfilepath = './'
	with open('austen_sents.txt', encoding='utf-8') as infile:
		for line in infile:
			words = word_tokenize(line)
			for word in words:
				with open(outfilepath + 'austen_words.txt', 'a') as outfile:
					outfile.write(word + ' ')
			with open(outfilepath + 'austen_words.txt', 'a') as outfile:
				outfile.write('\n')


def main():
	long_text()
	sents()
	words()
			


if __name__ == '__main__':
	main()
