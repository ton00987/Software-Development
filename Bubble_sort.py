import random
import time
from tkinter import *

lst = [random.randint(1, 10) for i in range(10)]
all_data = []
print(lst)

root = Tk()
root.title('Bubble sort')

canvas = Canvas(root, width=1000, height=650)
canvas.pack()

for i in range(len(lst)):
    all_data.append(canvas.create_rectangle((95*i)+25, 550-(50*lst[i]), (95*(i+1))+15, 600, fill='blue'))

while True:
    have_no_complicated = True

    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            for j in range(95):
                canvas.move(all_data[i], 1, 0)
                canvas.move(all_data[i+1], -1, 0)
                root.update()
                time.sleep(0.005)
            all_data[i], all_data[i+1] = all_data[i+1], all_data[i]
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(lst)
            have_no_complicated = False

    if have_no_complicated:
        break

print(lst)

root.mainloop()