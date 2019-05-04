# list comprehension

# [출력표현식 for 요소 in 입력 Sequence  [if 조건식]]

dataset = [4,True,'Dave',2.1,3]

int_data = [num for num in dataset if type(num) ==int]
print(int_data)
print(type(int_data))
int_square_data = [num * num for num in dataset if type(num) == int]
print(int_square_data)

un = []
print_until100 = [num for num in range(1,101)]
print(print_until100)
print_until = [num for num in range(1,101) if num % 3 ==0]
print_until2 = [num for num in range(1,101) if not num % 3 == 0 or num % 7 ==0]
print(print_until)
print(print_until2)

# Set comprehension
#{출력표현식 for 요소 in 입력 Sequence [if 조건식]}

int_data = [1,1,2,3,3,4]
square_data_set = { num * num for num in int_data if num >3 }
print(square_data_set)

#Dictionary comprehension
#{Key:Value for 요소 in 입력 Sequence [if 조건식]}

id_name = {1:'Dave',2:'Davie',3:'Anthony'}
print(id_name.items()) #dict_items([(1, 'Dave'), (2, 'Davie'), (3, 'Anthony')])
name_id = {val:key for key,val in id_name.items() if key >1}
print(name_id)

name_id2 = {key:val for key,val in id_name.items() if key >1}
print(name_id2)

name_id = {key * 10:val for key,val in id_name.items()}
print(name_id)

