people = 30
cars = 40
trucks = 15

if cars>people:
    print "We should take cars"
elif cars<people:
    print "We shold not take cars"
else:
    print "We cant decide"
    
if trucks >cars:
    print "thats too many trucks"
elif trucks<cars:
    print "Maybe we could take the trucks"
else:
    print "still cant decide"
    
if people>trucks:
    print "alright lets take the trucks"
else:
    print "Fine lets stay home"
