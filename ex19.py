def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "you have %d cheeses!"%cheese_count
	print "you have %d boxes of crackers "%boxes_of_crackers
	print "man thats enough for party"
	print "get a blanket \n"

print "We can give the numbers directly"
cheese_and_crackers(20,30)

print "Or we can use variable from script"
amt_of_cheese =20
amt_of_crackers = 30
cheese_and_crackers(amt_of_cheese,amt_of_crackers)

print "We can do maths inside to"
cheese_and_crackers(20+6,36+15)

print "And we can combine variable with maths"
cheese_and_crackers(amt_of_cheese+19,amt_of_crackers+21)