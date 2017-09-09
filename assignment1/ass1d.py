num = [2,6,9,8,4,12,15,27]


#def is_divisible_by_two(number):
	#return(number % 2 == 0)

for number in num:
	if number % 2 ==0:
		print("{} is a multiple of two".format(number))
	elif number % 3 == 0:
		print("{} is a multiple of three".format(number))
	elif (number % 2==0) and (number % 3==0):
		print("{} its a multiple of two or three".format(number))
	else:
	    print("{} its neither a multiple of two or three".format(number))

