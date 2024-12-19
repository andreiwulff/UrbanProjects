def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(i, position)] = string
    return strings_positions

info = [
    'Text to tell.',
    'Use encoding utf-8.',
    'Because there are 2 languages!',
    'Thank you!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
