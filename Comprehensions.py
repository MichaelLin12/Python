#List Comprehensions

# output_list = 
# [output_exp for var in input_list if (var satisfies this condition)]

# Note that list comprehension may or may not contain an if condition. 
# List comprehensions can contain multiple for (nested list comprehensions).

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
output_list = []
  
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
  
list_using_comp = [var for var in input_list if var % 2 == 0]
  
print("Output List using list comprehensions:",
                               list_using_comp)


list_using_comp = [var**2 for var in range(1, 10)]
  
print("Output List using list comprehension:", 
                              list_using_comp)


# Dictionary comprehensions

# output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

input_list = [1,2,3,4,5,6,7]
  
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
  
print("Output Dictionary using dictionary comprehensions:",
                                           dict_using_comp)

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
  
dict_using_comp = {key:value for (key, value) in zip(state, capital)}
  
print("Output Dictionary using dictionary comprehensions:", 
                                           dict_using_comp)


# Set comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
  
set_using_comp = {var for var in input_list if var % 2 == 0}
  
print("Output Set using set comprehensions:",
                              set_using_comp)