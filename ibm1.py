#!/usr/bin/python
# -*- coding: utf-8 -*-

# EM-IBM1, Expectation Maximization
# Alexandre Pais Gomes
# Master ISI

# Opening the files
source = open("resources/d10t10.SOURCE.en", "r")
target = open("resources/d10t10.REFERENCE.fr", "r")

# Source
S = source.read() # Sentences
s = S.split() # Words

# Target
T = target.read() # Sentences
t = T.split() # Words

# Probability initialization of p(t|s) (equiprobable)
# This whole initialization may be useless (to check later on)
p = {}
how_many_t = 0.
for words_t in t:
	how_many_t += 1.
	#for words_s in s:
		#p[(words_t, words_s)] = 1/how_many_t # I shouldn't be using this I guess (to resolve)


total = {}
count = {}
t_total = {}


# While non-convergence
for i in range(1):
	# Initialization
	for l1 in s:
		total[l1] = 0
		#for l2 in t:
		#	count[(l2,l1)] = 0
		# To do: see if it's important (or not) to initialize it
	
	# For each pairs of sentences (S,T)
	#for l1 in S:
	#	for l2 in T:
	#		for words_t in t:
	#			t_total[words_t] = 0
	#			for words_s in s:
	#				t_total[words_t] += p[(words_t, words_s)]

# Closing the files
source.close()
target.close()