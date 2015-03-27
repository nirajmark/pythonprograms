the_count = [1,2,3]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies',2 , 'dimes', 3, 'quarters']

#this is first for loop
for number in the_count:
	print "This is count %d"% number
	
for fruit in fruits:
	print "A fruit of type %s"% fruit
	
for i in change:
	print " I got %r"% i
	
#Building the list
elements = []

# then use range function to do 0 to 5 count
for i in range(0, 6):
	print "Adding %d to list"% i
	# append - to add item in list
	elements.append(i)
	
	
# now we can print them out too
for i in elements:
	print "Element is %d"% i
	

