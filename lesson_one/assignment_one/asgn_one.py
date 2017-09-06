'''
	Find the First Assignment in README.md  
	and come back here and and answer the questions 
	Happy coding!
'''

#Present Your Answers Below

#Question[1]
print("I am Charles Opoku Agyemang from Ghana and from a family of 6 kids who schooled at MEST and now serves as a CTO in vendyads")

#Question[3]
def doubler(number):
	return number * 2

#test cases 2 = 4 and  3 = 6
print(doubler(2))
print(doubler(3))


#Question[4]
def age_checker(age):
	if age < 20:
		return "You are young"
	else  :
		return "You are old"	
# test cases 20 => "You are old" and 19 => "You are young"	
print(age_checker(20))	
print(age_checker(19))

#Question[5]
def multiple_of_two_and_three_checker(number):
		
		is_a_muliple_two 			    =  number % 2 == 0
		is_a_multiple_of_three 			=  number % 3 == 0
		is_a_multiple_of_two_or_three 	=  is_a_muliple_two or is_a_multiple_of_three
		is_a_muliple_of_two_and_three 	=  is_a_muliple_two and is_a_multiple_of_three


		if is_a_multiple_of_two_or_three and number != 0 :
				#bigger pickture
				if is_a_muliple_two and is_a_multiple_of_three:
					return "is a multiple of two and three"
				elif is_a_muliple_two:
					return "is a multiple of two"
				elif is_a_multiple_of_three:
					return "is a multiple of three"	
		else :
			return "its neither a multiple of two or three"			
						


				

# test cases 2 => is a multiple of two , 
# 			 9 => is a multiple of three ,  
# 			12 => is a muliple of two and three , 
#			 5 => neither...

print(multiple_of_two_and_three_checker(2))
print(multiple_of_two_and_three_checker(9))
print(multiple_of_two_and_three_checker(12))
print(multiple_of_two_and_three_checker(5))


