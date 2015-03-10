#!/usr/bin/python
# -*- coding: utf-8 -*-

# EM-IBM1, Expectation-Maximization Algorithm
# Alexandre Pais Gomes
# Master ISI

# Probability initialization of p(t|s) (equiprobable for each tuple)
# This whole initialization may be useless (to check later on)
p = {}
total = {}
count = {}
t_total = {}

how_many_words_in_t = len(open("resources/d10t10.REFERENCE.fr").read().split())
how_many_lines = len(open("resources/d10t10.SOURCE.en").readlines())

# While non-convergence
for i in range(1):
	# Initialization
	for ls in (open("resources/d10t10.REFERENCE.fr").read().split()):
		total[ls] = 0
		#for l2 in t:
		#	count[(l2,l1)] = 0
	
	# Opening the files
	source = open("resources/d10t10.SOURCE.en", "r")
	target = open("resources/d10t10.REFERENCE.fr", "r")

	# For each pairs of sentences (S,T)
	for i in range(how_many_lines):
		ls = source.readline()
		lt = target.readline()
		for words_lt in lt.split():
			if(words_lt not in t_total):
				t_total[words_lt] = 0
			for words_ls in ls.split():
				if((words_lt, words_ls) not in p):
					p[(words_lt, words_ls)] = 1./how_many_words_in_t
				t_total[words_lt] += p[(words_lt, words_ls)]

print t_total

