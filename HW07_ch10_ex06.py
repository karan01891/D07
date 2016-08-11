# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
import copy

lst = [1,44,5]
op = [0,1,2]

def is_sorted(lst):
	lt = copy.deepcopy(lst)
	#print (lt)
	lst.sort()
	#print (lst)
	if lt == lst:
		return True
	else:
		return False



def main():
	pass

if __name__ == '__main__':
    main()

print (is_sorted(lst))
print (is_sorted(op))
	