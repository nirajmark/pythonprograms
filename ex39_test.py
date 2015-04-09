import hashmap

#create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states,'Oregon','OR')
hashmap.set(states,'Florida','FL')
hashmap.set(states, 'California','CA')
hashmap.set(states, 'New York','NY')
hashmap.set(states, 'Michigan','MI')

#create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI' ,'Detroit')
hashmap(cities,'FL','Jacksonville')

# add some more cities
hashmap.set(cities,'NY','New York')
hashmap.set(cities,'OR','Portland')

#print out some cities
print '-'*20
print "NY state has: %s"%hashmap.get(cities,'NY')
print "OR state has: %s"%hashmap.get(cities,'OR')

# print some state
print "-"*20
print "Michigan abv is: %s"%hashmap.get(states,'Michigan')
print "Florida abv is: %s"%hashmap.get(states,'Florida')

#do it using the states then cities dict
print "-"*20
print "Michigan has: %s"%hashmap.get(cities,hashmap.get(states,'michigan')) 

#print every state abv
print "-"*20
hashmap.list(states)
