user_input = input("Введіть текст (латиниця та цифри):")
text_lower = user_input.lower()

max_count = 0
current_count = 1

if len(user_input) > 0:
    for i in range(len(user_input) - 1):
        if user_input[i] == user_input[i+1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 1
    if current_count > max_count:
        max_count = current_count
else:
    max_count = 0

vowels_set = {"a","e","i","o","u","y"}
consonants_set = {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"}

v_count = 0
c_count = 0

for char in text_lower:
    if char in vowels_set:
        v_count+=1
    elif char in consonants_set:
        c_count +=1

found_vowels = set(text_lower).intersection(vowels_set)
result_vowels = sorted(list(found_vowels))

print("\n" + "="*40)
print(f"Аналіз тексту: '{user_input}'")
print("="*40)
print(f"1. Макс. кількість однакових символіа підряд: {max_count}")
print(f"\n2. Голосних: {v_count}, Приголосних:{c_count}")
if v_count > c_count:
    print("Результат: Більше голосних літер.")
elif c_count > v_count:
    print("Результат: Більше приголосних літер.")
else:
    print("Результат: Кількість однакова.")

print("\n3. Унікальні голосні за абеткою: ", end=" ")
if result_vowels:
    print(",".join(result_vowels))
else:
    print("Не знайдено")
print("="*40)
