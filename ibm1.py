#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

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

# Source and target paths (change here if needed)
source_path = "resources/d10t10.SOURCE.en"
target_path = "resources/d10t10.REFERENCE.fr"

how_many_words_in_t = len(open(target_path).read().split())
how_many_lines = len(open(source_path).readlines())

delta_plx = 1
plx = 0
iteration_nb = 0

PLX_PRECISION = -1
# Getting the delta (from the user or arbitrary)
if(len(sys.argv) == 2):
	argument = float(sys.argv[1])
	if(argument >= 0 and argument <= 1):
		PLX_PRECISION = float(sys.argv[1])

if(PLX_PRECISION == -1):
	PLX_PRECISION = 0.005 # Approximately 20 iterations

print 'Starting with delta = ' + str(PLX_PRECISION)
# While non-convergence
while(delta_plx > PLX_PRECISION):
	total = {}
	count = {}
	t_total = {}

	# Opening the files
	print 'Initializing iteration ' + str(iteration_nb+1) + '...'
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
	
	###############################
	#### Perplexity evaluation ####
	###############################
	print '   Evaluating perplexity...',
	log_sum = 0
	size_m = 0
	maxi = {}
	for (a,b),prb in p.items():
		maxi[a] = max(maxi.get(a,0), prb)
	#endfor
	for w,prb in maxi.items():
		size_m += 1
		log_sum += math.log(prb,2)
	#endfor
	#plx = pow(2, (-1/size_m)*log_sum)
	new_plx = -log_sum/size_m
	if(plx == 0):
		delta_plx = 1
	else:
		delta_plx = plx - new_plx
	plx = new_plx
	print repr(plx)
	
	iteration_nb += 1
#endfor

# Writing the results in a file
print 'Perplexity reached delta\n',
print 'Preparing final output...',
sys.stdout.flush()
output = open("probabilities.txt", "w")
s = ''
for (a,b),y in p.items():
	s += repr(a) + " " + repr(b) + " " + repr(y) + '\n'
output.write(s + '\n')
output.close()
print 'OK'
