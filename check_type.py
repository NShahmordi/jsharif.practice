def check_type(input_list):
    counter_True = 0
    result_item = 0
    result_item = input_list[0]
    for i in input_list:
        if type(i) == type(result_item):
            counter_True += 1
        else:
            continue    
    if counter_True == len(input_list):
        return True
    else:
        return False
obj1 = check_type([1,2,3,'str'])
obj2 = check_type([1,2,3])    
print(obj1)
print(obj2)