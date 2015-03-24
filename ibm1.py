#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

######################################################
#### EM-IBM1 : Expectation-Maximization Algorithm ####
######################################################
# Alexandre Pais Gomes
# Master ISI

#########################
#### Initializations ####
#########################
# Probability initialization of p(t|s) (equiprobable for each tuple)
p = {}
total = {}
count = {}
t_total = {}

# Source and target paths (change here if needed)
source_path = "resources/d10t10.SOURCE.en"
target_path = "resources/d10t10.REFERENCE.fr"

# Getting the given number of iterations wanted
iteration = 1 # Number of iterations (1 by default)
if (len(sys.argv) == 2):
	iteration = int(sys.argv[1])
	print 'Setting the number of iteration at ' + str(iteration)
else:
	print 'Setting the number of iteration at ' + str(iteration) + ' (by default)'
#endif

how_many_words_in_t = len(open(target_path).read().split())
how_many_lines = len(open(source_path).readlines())

# While non-convergence
for i in range(iteration):
	# Opening the files
	print 'Initializing iteration ' + str(i+1) + '...'
	source = open(source_path, "r")
	target = open(target_path, "r")

	print '   Normalization and counting...',
	sys.stdout.flush()
	# For each pairs of sentences (S,T)
	for i in range(how_many_lines):
		ls = source.readline()
		lt = target.readline()

		#######################
		#### Normalization ####
		#######################
		for words_lt in lt.split():
			if(words_lt not in t_total):
				t_total[words_lt] = 0
			#endif
			for words_ls in ls.split():
				if((words_lt, words_ls) not in p):
					p[(words_lt, words_ls)] = 1. / how_many_words_in_t
				#endif
				t_total[words_lt] += p[(words_lt, words_ls)]
			#endfor
		#endfor

		##################
		#### Counting ####
		##################
		for words_lt in lt.split():
			for words_ls in ls.split():
				if((words_lt, words_ls) not in count):
					count[(words_lt, words_ls)] = 0
				#endif
				count[(words_lt, words_ls)] += p[(words_lt, words_ls)] / t_total[words_lt]
				if(words_ls not in total):
					total[words_ls] = 0
				#endif
				total[words_ls] += p[(words_lt, words_ls)] / t_total[words_lt]
			#endfor
		#endfor
	#endfor
	print 'OK'

	###################################
	#### Probabilities estimations ####
	###################################
	# Re-opening the files
	source = open(source_path, "r")
	target = open(target_path, "r")

	print '   Probabilities estimations...',
	sys.stdout.flush()
	for i in range(how_many_lines): # There's probably a better way to do this
		ls = source.readline()
		lt = target.readline()
		for words_ls in ls.split():
			for words_lt in lt.split():
				p[(words_lt, words_ls)] = count[(words_lt, words_ls)] / total[words_ls]
			#endfor
		#endfor
	#endfor
	print 'OK'
	
	# A few tests
	print '      documents -> documents : ' + str(p[('documents', 'documents')])
	print '      par -> documents : ' + str(p[('par', 'documents')])
#endfor

# Writing the results in a file
print 'Preparing final output...',
sys.stdout.flush()
output = open("probabilities.txt", "w")
s = ''
for (a,b),y in p.items():
	s += repr(a) + " " + repr(b) + " " + repr(y) + '\n'
#output.write(repr(p) + '\n')
output.write(s + '\n')
output.close()
print 'OK'
