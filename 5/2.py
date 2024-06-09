def read_numbers(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_sorted_numbers(filename, numbers):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + '\n')


input_filename = "5\\2input.txt"
output_filename = "5\\2output.txt"

numbers = read_numbers(input_filename)
sorted_numbers = sorted(numbers)

write_sorted_numbers(output_filename, sorted_numbers)

