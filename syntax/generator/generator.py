def current_value(target_list):
    current_index = 0

    while current_index < len(target_list):
        yield target_list[current_index]
        current_index += 1


src_list = ["a", "b", "c"]
# <generator object current_value at ********************>
print(current_value(src_list))

for value in current_value(src_list):
    print(value)

# a
# b
# c
