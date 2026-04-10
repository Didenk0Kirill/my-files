import list_operations as lo

numbers = [10,2,5,2,8,1,9,3,4,7,6,5]
print("Початковий список: ", numbers)
print("1. Сортування:",lo.sort_list(numbers))
print("2.Пошук індексу числа 8:",lo.find_element(numbers,8))
print("3.Пошук послідовності[9,3,4]:",lo.find_sequence(numbers,[9,3,4]))
print("П'ять мінімальних:",lo.top_five_min(numbers))
print("П'ять максимальних:",lo.top_five_max(numbers))
print("Середнє арефметичне:",lo.get_average(numbers))
print("Без повторів:",lo.remove_duplicates(numbers))