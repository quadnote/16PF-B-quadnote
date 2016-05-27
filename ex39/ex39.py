#-*-coding:utf8

#create a mapping of state to abbreviation
states = {
    'Orangon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Hawaii' : 'HI'
}

# create a basic set of state and some cities in them
cities = {
    'CA' : 'San frasisco',
    'HI' : 'Detroit',
    'FL' : 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

#print some states
print('-' *10)
print("Hawaii's abbreviation is: %s" % states['Hawaii'])
print("Florida's abbreviation is: %s" % states['Florida'])

#print every state abbreviation
print('-' * 10)
print("stats = %s" % states)
print("states.items() = %s" % str(states. items))
print('-' *10)
for state, abbrev in states. items():
    print("%s is abbreviated %s" % (state, abbrev))

#print every city in state
print('-' * 10)
for abbrev, city in cities. items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states. items():
    print("%s state is abbreviated %s and has city %s" %(
        state, abbrev, cities[abbrev]
    ))

print('-' * 10)
# safety get a abbreviation by state that sight not be there
state = states. get('Texax')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Not Entered Yet')
print ("The city for the state 'TX' is: %s" % city)
