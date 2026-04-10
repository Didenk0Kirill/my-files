import os
import io

def create_file(filename,data):
    with io.open(filename, 'w') as f:
        for name, score in data:
            f.write(f"{name}:{score}\n")

def append_to_file(filename,name,score):
    with io.open(filename, 'a') as f:
        f.write(f"{name}:{score}\n")

def find_files_by_extension(extension=".txt"):
    return [f for f in os.listdir(".") if f.endswith(extension)]

def search_student(filename,search_name):
    with io.open(filename, 'r') as f:
        for line in f:
            if search_name.lower() in line.lower():
                return line.strip()
    return None

def sort_student_by_score(filename):
    student = []
    with io.open(filename, 'r') as f:
        for line in f:
            if ":" in line:
                parts = line.strip().split(":")
                student.append((parts[0],float(parts[1])))
                student.sort(key=lambda x: x[1], reverse=True)
                with io.open(filename, 'w') as f:
                    for name, score in student:
                        f.write(f"{name}:{score}\n")

data_list = [("Іваненко",85.5),("Петренко",92.0),("Сидоренко",78.3)]
file_name = "student.txt"
create_file(file_name,data_list)
append_to_file(file_name, "Коваленко",88.4)
sort_student_by_score(file_name)
print(find_files_by_extension())
print(search_student(file_name,"Іваненко"))