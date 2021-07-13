# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	a = str(eggs)
	for i in a:
		if eggs <= 12:
			return 1
		elif(i[0]<i[1]):
			return i[0]
		else: 
			return i[1]
