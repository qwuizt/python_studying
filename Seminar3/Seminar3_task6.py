def custom_sort(word_to_sort):
    return len(word_to_sort), word_to_sort


text = input("Введите текст: ")

words = text.split()

words.sort(key=custom_sort)

max_word_length = len(words[-1])

line_format = f"{{:>{max_word_length}}} {{}}"

for i, word in enumerate(words, start=1):
    print(line_format.format(word, i))
