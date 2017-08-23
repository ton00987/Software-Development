import random
import matplotlib.pyplot as plt

x_coor = []
y_coor = []
result = []

# Generate coordinates
for i in range(5):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    x_coor.append(x)
    y_coor.append(y)

min_x_coor = []
min_y_coor = []

def near(x_coor, y_coor):
    '''
    Define first point as a starting point
    then calculate all distances between starting point and others
    '''

    all_dis = []

    # Stop when It remains one coordinate
    if len(x_coor) == 1:
        return

    # Calculate distance
    for i in range(1, len(x_coor)):
        delta_x = x_coor[0] - x_coor[i]
        delta_y = y_coor[0] - y_coor[i]
        distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
        all_dis.append(distance)

    # Grab a minimum distance
    result.append(min(all_dis))
    # Search for coordinate
    min_index = all_dis.index(min(all_dis))
    min_x_coor.append(x_coor.pop(0))
    min_y_coor.append(y_coor.pop(0))

    # Swap coordinates
    x_coor[min_index], x_coor[0] = x_coor[0], x_coor[min_index]
    y_coor[min_index], y_coor[0] = y_coor[0], y_coor[min_index]

    near(x_coor, y_coor)

near(x_coor, y_coor)

# Add last point
min_x_coor.append(x_coor[0])
min_y_coor.append(y_coor[0])

# Add distance between starting point and last point
result.append(((min_x_coor[0] - min_x_coor[-1]) ** 2 + (min_y_coor[0] - min_y_coor[-1]) ** 2) ** 0.5)

min_x_coor.append(min_x_coor[0])
min_y_coor.append(min_y_coor[0])

print(sum(result))

plt.plot(min_x_coor, min_y_coor, 'bo', min_x_coor, min_y_coor, 'k')
plt.show()