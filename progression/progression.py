################################################################################################
#	name:	progression.py
#	desc:	identify type of progression
#	date:	2018-09-08
#	Author:	conquistadorjd
################################################################################################

import numpy

def type_of_progression(input_sequence):

	delta = []
	current = 0
	while current < len(input_sequence)-1:

		delta.append(input_sequence[current+1]-input_sequence[current])
		current = current+1

	delta_unique= set(delta)
	if len(delta_unique) == 1 :
		return "arithmetic"
	
	delta = []
	current = 0
	while current < len(input_sequence)-1:

		delta.append(input_sequence[current+1]/input_sequence[current])
		current = current+1

	delta_unique= set(delta)
	if len(delta_unique) == 1 :
		return "geometric"

	delta = []
	current = 0
	while current < len(input_sequence)-1:

		delta.append(1/input_sequence[current+1]-1/input_sequence[current])
		current = current+1

	delta_unique= set(delta)
	if len(delta_unique) == 1 :
		return "harmonic"
	else:
		return "nothing"

print('*** Program Started ***')

input_sequence = input('Please input sequence separated by "," : ')
input_sequence = eval('[' + input_sequence + ']')


result = type_of_progression(input_sequence)
print("result :" , result)

print('*** Program Ended ***')