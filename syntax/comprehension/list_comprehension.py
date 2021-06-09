""" リスト内包表記 """
# [1, 2, 3, 4, 5]
number_list = list(range(1, 6))

# 使わない場合
result_list = []
for number in number_list:
    result_list.append(number * 3)

# result_list = [3, 6, 9, 12, 15]
print("result_list =", result_list)

# 使った場合
result_list2 = [number * 3 for number in number_list]

# result_list2 = [3, 6, 9, 12, 15]
print("result_list2 =", result_list2)

# result_list3 = [2, 4]
result_list3 = [number for number in number_list if number % 2 == 0]
print("result_list3 =", result_list3)
