result_dict = {}
def same_parameter(input_list):
    counter_number = 0 
    for i in input_list:
        result_dict.setdefault(i ,0)
        result_dict[i] += 1
            
    for k,v in result_dict.items():
        if v == 1:
            counter_number += 1
            
    if counter_number == len(input_list):
        return 'True'
    else:
        return 'False'   
print(same_parameter([1,2,3,4,5,6]))
print(same_parameter([1,2,2,3,4,5,6]))
   

