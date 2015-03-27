# this one is like your script with argv
def print_two(*args):
	arg1,arg2 = args
	print "arg1: %r, arg2: %r"%(arg1,arg2)

#ok *args is pointless.
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r"%(arg1,arg2)

#this just take one argument
def print_one(arg1):
	print "arg1: %r"%arg1

# no arguments
def print_none():
	print "I got nothing"

print_two("Niraj","Mark")
print_two_again("Niraj","Mark")
print_one("Niraj")
print_none()