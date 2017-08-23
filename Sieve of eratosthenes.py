import time
from tkinter import *

last_number = int(input('Enter last number of prime range: '))
origin = list(range(2, last_number + 1))
print(origin)

# Check row of table
can_row = last_number % 10

# Add row
if can_row == 0:
    y_column = int(last_number / 10)
else:
    y_column = int(last_number / 10) + 1

root = Tk()
root.title('Sieve of eratosthenes')

canvas = Canvas(root, width=500, height=y_column*50)
canvas.pack()

all_text = []
num = 1

# Create table
for j in range(y_column):
    for i in range(10):
        all_text.append(canvas.create_rectangle(i * 50, j * 50, (i+1) * 50, (j+1) * 50, fill='lawn green'))
        canvas.create_text((50 * i) + 25, (50 * j) + 25, text=num)
        num += 1

# Set first element and other elements out of range to another color
canvas.itemconfig(all_text[0], fill='gray95')
for i in range(can_row):
    canvas.itemconfig(all_text[-1-i], fill='gray95')

k = 0
p = 2
c = 0

while p ** 2 < last_number:
    compare_list = []
    can_color = ['blue', 'red', 'yellow', 'orange']

    # Create list for compare
    for i in range(2, int(last_number/p) + 1):
        compare_list.append(p * i)

    print(compare_list)

    # Change element colors which isn't prime
    for i in range(len(all_text)):
        for l in range(len(compare_list)):
            if compare_list[l] == (i+1):
                canvas.itemconfig(all_text[i], fill=can_color[c])
                root.update()
                time.sleep(0.1)

    # Delete element which isn't prime
    origin = list(set(origin).difference(set(compare_list)))
    origin.sort()

    c += 1
    k += 1
    p = origin[k]

    if c == len(can_color):
        c = 0

print(origin)

root.mainloop()
#class UI(object):
#    def __init__(self):
#        y_column = int(last_number / 10) + 1
#        print(y_column)
#        self.root = Tk()
#        self.root.title('Sieve of eratosthenes')
#        self.all_text = []
#        num = 0
#        for j in range(y_column):
#            for i in range(10):
#                self.all_text.append(Label(self.root, text=num+1, bg='light gray', width=5, height=2, relief='groove'))
#                self.all_text[num].grid(row=j, column=i)
#                num += 1

#        self.change_bg()
#        self.root.mainloop()

#    def change_bg(self):
#        self.all_text[0].config(bg='blue')
#        self.root.update()
#        time.sleep(5)
#        self.all_text[2].config(bg='blue')
#        self.root.update()
#        time.sleep(5)
#        self.all_text[4].config(bg='blue')
#        self.root.update()
#        time.sleep(5)

#UI()