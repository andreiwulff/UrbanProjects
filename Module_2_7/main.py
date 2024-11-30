# import tkinter as tk
# def get_values():
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     return num1, num2
# def insert_values(values):
#     answer_entry.delete(0, values)
# def add():
#     num1, num2 = get_values()
#     res = num1 + num2
#     insert_values(res)
#
#
#
#
#
# window = tk.Tk()
# window.title('CALCULATOR')
# window.geometry('350x350')
# window.resizable(False, False)
# button_add = tk.Button(window, text='+', width=2, height=2)
# button_add.place(x=100, y=200)
# button_sub = tk.Button(window, text='-', width=2, height=2)
# button_sub.place(x=150, y=200)
# button_mul= tk.Button(window, text='*',width=2, height=2 )
# button_mul.place(x=200, y=200)
# button_div = tk.Button(window, text='/', width=2, height=2)
# button_div.place(x=250, y=200)
# number1_entry = tk.Entry(window, width=28)
# number1_entry.place(x=100, y=75)
# number2_entry = tk.Entry(window, width=28)
# number2_entry.place(x=100, y=150)
# answer_entry = tk.Entry(window, width=28)
# answer_entry.place(x=100, y=300)
# number1 = tk.Label(window, text="Enter first number")
# number1.place(x=100, y=50)
# number2 = tk.Label(window, text="Enter second number")
# number2.place(x=100, y=125)
# answer = tk.Label(window, text="ANSWER")
# answer.place(x=100, y=275)
# window.mainloop()

def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    elif isinstance(data, int):
        total_sum += data
    elif isinstance(data, str):
        total_sum += len(data)

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
