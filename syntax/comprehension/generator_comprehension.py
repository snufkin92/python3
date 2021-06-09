""" ジェネレータ内包表記 """
numbers = (num * 3 for num in range(1, 6))

# <generator object <genexpr> at ********************>
print(numbers)

for value in numbers:
    print(value)

# 3
# 6
# 9
# 12
# 15
