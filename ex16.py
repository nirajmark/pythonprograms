from sys import argv

script,filename = argv

print "We are going to erase %r"%filename
print "if you dont want that hit ctrl+C(^c)"
print "If you dont want that hit return"

raw_input("?")

print "opening the file.."
target = open(filename,'w')

print "Truncate the file goodbye!"
target.truncate()

print "Now I'm going to ask for three lines"
line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "I'm going to write that in file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally we close it"
target.close()