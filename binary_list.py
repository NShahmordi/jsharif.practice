str_counter = 0
str_list = []

def zero_pow(binary_str:str):
    for i in binary_str:
        if i == '0':
            str_counter += 1
            str_list.append(str_counter)
        else:
            str_counter = 0
            continue   
        
    pow_of_zero = max(str_list)
    return ('0' * pow_of_zero)
    
print(zero_pow('100001101010000000'))        
   
     