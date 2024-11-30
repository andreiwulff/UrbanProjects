

# def summator(txt,*values):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s}'
#
# print(summator('SUMMATION:', 2, 3, 4))


# def info(value, *types, name_author='Den', '**values):
#     print('TYPE:', type(values))
#     print('VARIABLE:', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
# info('EXAMPLE OF USING ALL TYPES OF PARAMETERS', 2, 3, 4, name_author ='Denis', name='Den', course='Python')




def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        lower_word = word.lower()
        if root_word in lower_word or lower_word in root_word:
            same_words.append(word)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)