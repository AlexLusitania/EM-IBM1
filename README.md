# EM-IBM1
Expectation-Maximization Algorithm in Python

## How to use it?
```
$ git clone https://github.com/AlexLusitania/EM-IBM1.git ibm1
$ cd ibm1
$ python ibm1.py [given_delta]
```
The delta must be between 0 and 1. It will be 0.005 by default. Knowing that the bigger is the delta, the lower will be the precision of the output probabilities.

When executed, the script will create a output file called **probabilities.txt** containing all the words (source and target) and the associated probability.

**NB**: The original text (in French) and its translation (in English) are in the **resources/** folder, change the path in the code if needed
