class Person:
    def __init__(self, first_name:str, favourite_food:list, bad_food:list):
        self.first_name = first_name
        self.favourite_food = favourite_food
        self.bad_food = bad_food
        
    
    def taste(self, food:str,first_name:str, favourite_food:list):
        self.food = food
        if food in favourite_food:
            return f'{first_name} eats {food} and loves it!'
        else:
            return f'{first_name} doesn\'t like it!'

obj1 = Person('Bahar',['pizza','hamburger', 'chicken'] ,['shrimp', 'fish'])
print(obj1.taste('fish','Bahar',['pizza','hamburger', 'chicken']))
