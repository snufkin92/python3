""" リスト内包表記 """
word = "apple"

letter_count = {char: word.count(char) for char in word}
# letter_count = {char: word.count(char) for char in set(word)}

# letter_count = {'a': 1, 'p': 2, 'l': 1, 'e': 1}
print("letter_count =", letter_count)

# set_letter = {'e', 'p', 'a', 'l'}
set_letter = {char for char in set(word)}
print("set_letter =", set_letter)
