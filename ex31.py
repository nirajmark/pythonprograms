print "You are entering the dark room with two doors. Which door do you choose 1 or 2"

door = raw_input('>')

if door == '1':
    print "Giant bear eating cheese cake is waiting for you"
    print "1: Take the cake"
    print "2: Scream at the bear"
    
    bear = raw_input('>')
    
    if bear == '1':
        print "Bear eat your face:D"
    elif bear == '2':
        print "the bear eats your leg"
    else:
        print "doing %s is better bear runs away"%bear
        
      
elif door == '2':
    print "You stare into endless abiss"
    print "1: Blueberries"
    print "2: Yello jacket"
    print "3: Understanding revolver yelling melody"
    
    insanity = raw_input('>')
    
    if insanity == '1':
        print "you survived"
    else:
        print "The insanity rots your eye"
        
else:
    print "You die SmartAss"
