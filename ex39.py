#mapping of states to abbrevation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'JacksonVille'
}
    
#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '_' * 10
print "NY state has ", cities['NY']
print "Or states has ", cities['OR']

# print some states 
print '_' *10
print "Michigan abbrevation is ", states['Michigan']

#do it using states and then cities
print '_' *10
print "Michigan has ",cities[states['Michigan']]

#print every states abbrevation
print '_' *10
for  state,abb in states.items():
    print "%s state's abbrevation is %s"%(state,abb)
    
#safely get a abbrevation by state that might not be there
print '_' *10
state = states.get('Texas')
if not state:
    print "Sorry no texas"
    
# get a city with default value
city = cities.get('TX','Does not exist')
print "The city for texas is %s"%city 













