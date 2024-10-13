input_list =[1,8,6,2,5,4,8,3,7] #-> list(input('Enter a list:')) #
index_of_big_number =0
big_num = 0
counter_index = 0
len_input_list = len(input_list)
for i in input_list:
    if i > big_num:
        big_num = i
        index_of_big_number = input_list.index(i)

input_list.remove(big_num)
new_big_num = 0
new_index_of_big_number = 0
for i in input_list:
    if i == big_num:
        continue
    if i > new_big_num:
        new_big_num = i
        new_index_of_big_number = input_list.index(i)
    
print(big_num ,':', index_of_big_number,'and', new_big_num,":",new_index_of_big_number)
area_of_rect = (new_big_num) * (len_input_list - (index_of_big_number+1))
print(area_of_rect)
           
 
 
 
 
 
 
    
    

# counter_number = 0
# len_of_input_list = len(input_list)
# for i in input_list:
#     counter_number += 1
#     result = (sorted(input_list)[-1]) * (sorted(input_list)[-2])
    