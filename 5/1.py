def read_numbers(filename):
    with open(filename, 'r') as file:
        numbers = file.readline().split()
        numbers = [int(num) for num in numbers]
    return numbers

def write_product(filename, product):
    with open(filename, 'w') as file:
        file.write(str(product))


input_filename = "5\\input.txt"
output_filename = "5\\output.txt"

numbers = read_numbers(input_filename)
product = 1
for num in numbers:
    product *= num

write_product(output_filename, product)
