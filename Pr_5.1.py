def find_element_index(lst, value):
    indices = [i for i, x in enumerate(lst) if x == value]
    return indices

my_list = [10, 20, 30, 40, 50]
search_val = 20
result = find_element_index(my_list, search_val)
print(f"Список: {my_list}")
print(f"Індекс елемента {search_val}:{result}")