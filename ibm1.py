#!/usr/bin/python
# -*- coding: utf-8 -*-


# Opening the files
source = open("resources/d10t10.SOURCE.en", "r")
target = open("resources/d10t10.REFERENCE.fr", "r")

s = source.read().split()
t = target.read().split()

# Probability initialization p(t|s) (equiprobability)
wordcount = 0.
for word in t:
	wordcount += 1.
p = {}
for word in s:
	p[word] = 1/wordcount

count = {}
total = {}
# While non-convergence
for i in range(1):
	# Initialization
	for l1 in s:
		total[l1] = 0
		for l2 in target.read().split():
			count[l2, l1] = 0
	print count


# Closing the files
source.close()
target.close()