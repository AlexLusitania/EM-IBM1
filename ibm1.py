#!/usr/bin/python
# -*- coding: utf-8 -*-

######################################################
#### EM-IBM1 : Expectation-Maximization Algorithm ####
######################################################
# Alexandre Pais Gomes
# Master ISI

#########################
#### Initializations ####
#########################
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
	# Opening the files
	source = open("resources/d10t10.SOURCE.en", "r")
	target = open("resources/d10t10.REFERENCE.fr", "r")

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

	###################################
	#### Probabilities estimations ####
	###################################
	# Re-opening the files
	source = open("resources/d10t10.SOURCE.en", "r")
	target = open("resources/d10t10.REFERENCE.fr", "r")

	for i in range(how_many_lines): # There's probably a better way to do this
		ls = source.readline()
		lt = target.readline()
		for words_ls in ls.split():
			for words_lt in lt.split():
				p[(words_lt, words_ls)] = count[(words_lt, words_ls)] / total[words_ls]
			#endfor
		#endfor
	#endfor
#endfor

# Writing the results in a file
output = open("probabilities.txt", "w")
output.write(repr(p) + '\n')
output.close()
