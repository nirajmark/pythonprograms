def add(a,b):
	print "Adding %d+%d"%(a,b)
	return a+b

def sub(a,b):
	print "Substractin %d-%d"%(a,b)
	return a-b

def mult(a,b):
	print "Multiplying %d*%d"%(a,b)
	return a*b

def divide(a,b):
	print "Dividing %d / %d"%(a,b)
	return a/b

print "Lets do math with just functions"

age = add(30,5)
height = sub(78,4)
weight = mult(90,2)
iq = divide (200,2)

print "Age: %d, height: %d, weight: %d, iq:%d"%(age,height,weight,iq)


	