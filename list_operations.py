def sort_list(data):
    """Повертає відсортований список."""
    return sorted(data)
def find_element(data,value):
    """Пошук індексу елемента за значенням. Повертає індекс або None."""
    try:
        return data.index(value)
    except ValueError:
        return None

def find_sequence(data,sequence):
    """Пошук послідовності елементів у списку. Повертає індекс початку або -1"""
    n, m = len(data), len(sequence)
    for i in range(n - m + 1):
        if data[i:i+m] == sequence:
            return i
        return -1

def top_five_min(data):
    """Повертає перші п'ять мінімальних елементів."""
    return sorted(data)[:5]

def top_five_max(data):
    """Повертає перші п'ять максимальних елементів."""
    return sorted(data, reverse=True)[:5]

def get_average(data):
    """Повертає середнє арефметичне елементів списку."""
    return sum(data) / len(data) if data else 0

def remove_duplicates(data):
    """Повертає список без поворотів зберігаючи порядок першої появи."""
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result
