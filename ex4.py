cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
car_driven = drivers
carpool_capacity = car_driven*space_in_car
average_passengers_per_car = passengers/car_driven

print "There are",cars," cars available"
print "there are only",drivers," drivers available"
print "there will be",cars_not_driven," empty cars today"
print "we can transport",carpool_capacity," people today"
print "We have",passengers," to carpool today"
print "We need to put about",average_passengers_per_car," in each car"
