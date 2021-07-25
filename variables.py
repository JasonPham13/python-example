# school = "Higley High School"
# print(school)
#
# name = 'jason'
# print(name)
#
# print(name + " goes to " + school)
#
# favorite_food = 'Pizza'
#
# print("My name is " + name + " I go to " + school + " my favorite food is " + favorite_food)
#
# credits_taken = 14
# print(credits_taken)
#
# trained_astronauts = 563
# space_tourist = 7
# total_people_in_space = trained_astronauts + space_tourist
# print(total_people_in_space)
#
# miles_to_portland = 1425.81
# miles_to_helena = 907.29
# helena_to_portland = miles_to_portland - miles_to_helena
# print(helena_to_portland)
#
# popcorn_string = '4.25'
# popcorn_float = float(popcorn_string)
# bags_string = '3'
# bags_int = int(bags_string)
# cost = popcorn_float * bags_int
# print(cost)
#
# print('This semester I am taking ' + str(credits_taken))

# name = input('Please enter your name')
# print('Hello, ' + name)

name = input('Enter name of item: ')
sold_string = input('Enter quanity of ' + name + ' sold: ')
price_string = input('Enter price of ' + name + ': ')
total = int(sold_string) * float(price_string)
print('')
print( name + ' sales')
print('Quanity sold: ' + sold_string)
print('Unit Price: ' + price_string)
print('Total : ' + str(total))

