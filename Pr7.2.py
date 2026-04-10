def reverse_content(input_file, output_a, output_b):
    with open(input_file, 'r') as f:
        lines = f.readlines()

        reversed_lines = [line.strip()[::-1] for line in lines]
        with open(output_a,'w') as f:
            for line in reversed_lines:
                f.write(line + '\n')

        with open(output_b,'w') as f:
            for line in reversed(reversed_lines):
                f.write(line + '\n')
with open("source.txt","w") as f:
    f.write("Hello world\n")
    f.write("Python is cool\n")
    f.write("Programming is also cool")
reverse_content("source.txt","result_a.txt","result_b.txt")