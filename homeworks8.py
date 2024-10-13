#we need 4 wheels,1 body and 2 dummy to make a car.
number_of_bodies = int(input('Enter a number for bodies:'))
number_of_wheels = int(input('Enter a number for wheels:'))
number_of_dummies = int(input('Enter a number for dummies:'))

cars_counter = 0
all_values = 0
remainder_body = 0
remainder_wheel = 0
remainder_dummy = 0

all_value = number_of_wheels // 4
remainder_wheel = number_of_wheels % 4
all_value += number_of_dummies // 2 
remainder_dummy = number_of_dummies % 2
cars_counter = all_value // 2
remainder_body = number_of_bodies - cars_counter

print(f'''you can make {cars_counter} cars and we have {remainder_body} remainder bodies,
      {remainder_wheel} remainder wheels and {remainder_dummy} remaider dummy.''')                