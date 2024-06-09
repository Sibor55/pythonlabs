def read_children_info(filename):
    children_info = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            surname, name, age = parts[0], parts[1], int(parts[2])
            children_info.append((surname, name, age))
    return children_info

def write_child_info(filename, child_info):
    with open(filename, 'w') as file:
        for info in child_info:
            file.write(f"{info[0]} {info[1]} {info[2]}\n")


input_filename = "5\\children_info.txt"
oldest_filename = "5\\oldest_child.txt"
youngest_filename = "5\\youngest_child.txt"

children_info = read_children_info(input_filename)

oldest_child = max(children_info, key=lambda x: x[2])
youngest_child = min(children_info, key=lambda x: x[2])

write_child_info(oldest_filename, [oldest_child])
write_child_info(youngest_filename, [youngest_child])

