from tkinter import *


def calculate():
    miles = user_input.get()
    if miles != '':
        km = round(float(miles) * 1.609, 1)
        result_label.config(text=km)
    else:
        result_label.config(text='empty')


# WINDOW SETTINGS
window = Tk()
window.geometry('+800+400')
window.geometry('250x90')
window.title('MilesToKm')
window.minsize(width=250, height=90)
window.maxsize(width=250, height=90)
window.config(bg='#ff5745', padx=40, pady=15)

# USER ENTRY VALUE
user_input = Entry()
user_input.config(justify='center', width=5)
user_input.grid(column=1, row=0)

# MILES LABEL
miles_label = Label()
miles_label.config(bg='#ff5745', text='Miles')
miles_label.grid(column=2, row=0)

# KM LABEL
miles_label = Label()
miles_label.config(bg='#ff5745', text='Km')
miles_label.grid(column=2, row=1)

# IS EQUAL TO LABEL
is_equal_to_label = Label()
is_equal_to_label.config(bg='#ff5745', text='Is equal to')
is_equal_to_label.grid(column=0, row=1)

# RESULT LABEL
result_label = Label()
result_label.config(bg='#ff5745')
result_label.grid(column=1, row=1)

# CALCULATE BUTTON
calculate_button = Button()
calculate_button.config(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
