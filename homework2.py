import math
pi_number = math.pi

circle_number = int(input('Enter radius of a circle:'))

area_of_circle = (circle_number ** 2) * pi_number
circum_of_circle = 2 * pi_number * circle_number

print(f'area of circle = {area_of_circle}')
print(f'circum of circle = {circum_of_circle}')
