ten_things = "Apples oranges crows telephone light sugar"

print "Wait those are not ten things lets fix!!"

stuff = ten_things.split(' ')
more_stuff = ["day","night","songs","Frisbee","corn","Banana","Girl","Boy"]
while len(stuff)!=10:
    next_one = more_stuff.pop()
    print "Adding", next_one
    stuff.append(next_one)
    print "there are %d items now"%len(stuff)
    
print "There we go:",stuff

print "lets do things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5]) 
