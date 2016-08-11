# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

lst = ['karan','rao',['k','l',['o','p']]]



def capitalize(lst):
	lt = list()
	for x in lst:		
		if type(x) == list:
			lt.append(capitalize(x))


		else:
			x = x.upper()
			lt.append(x)
			
	return(lt)

def main():
	pass

main()	

print(capitalize(lst))


