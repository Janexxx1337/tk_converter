from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Converter")
window.minsize(width=300, height=300)
window.config(padx=50,pady=10)
# Labels

input_num = Entry(width=10)
input_num.grid(column=2, row=0)
miles = Label(text="Miles")
miles.grid(column=3, row=0)








is_equal = Label(text="is equal to")
is_equal.grid(column=1, row=1)
starting = Label(text=0)
starting.grid(column=2, row=1)
km = Label(text="Km")
km.grid(column=3, row=1)



def calc_sum():
    convert_sum = int(input_num.get()) * 1.60934
    starting.config(text=round(convert_sum))



calculate_btn = Button(text='Calculate', command=calc_sum)
calculate_btn.grid(column=2, row=2)














window.mainloop()

