import numpy as np
from random import randint

def randgen(domain, n, p):
	# the function only accepts lists for the vector of weights
	if type(p) != list:
		print('p must be a list')
		return
	# here we check that the sum of the vector of weights is equal to 1
	elif sum(p) != 1:
		print('sum of p must be equal to 1')
		return
	# check that every event has its own weight
	if len(domain) != len(p):
		print('the number of events in the discrete domain must be equal to the number of weights in P')
		return
	# check that every element in the domain is unique
	for value in domain:
		if domain.count(value) > 1:
			print('every element in the domain must be unique')
			return
	
	i = 0
	output_list = []
	samples_list = []
	
	# we first compute a list that contains every event in the domain w.r.t their weights
	# e.g if "H"'s weight is 0.2, there will 20 times 'H' in the list
	for weight in p:
		output_list.append(int(weight*100)*[domain[i]])
		i+=1
	
	# we join every list of output_list together in a samples_list
	for element in output_list:
		samples_list += element
	
	j = 0
	random_samples = []
	# then, we RANDOMLY select an element in the samples_list.
	# the output is stored in random_samples. We do this n times.
	while j < n:
		random_samples.append(samples_list[randint(0, len(samples_list)-1)])
		j+=1
	
	print(random_samples)
	for elt in domain:
		print("Number of {0} : {1}".format(elt, random_samples.count(elt)))

if __name__ == "__main__":
	randgen("HTXU", 10, [0.2, 0.4, 0.1, 0.3])	