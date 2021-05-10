from PIL import Image  
import random
import numpy as np
import csv
import pandas as pd


width = 50
height = 50

colors = ['#FF0000', '#FFFF00', '#008000']

imgs = []

train = []
for i in range(1,10):
    index = random.randint(0,2)
    img = Image.new( mode = "RGB", size = (width, height), color = colors[index])
    
    r = 0
    y = 0
    g = 0
    
    if index == 0:
        color = 'red'
        r = 1
    elif index == 1:
        color = 'yellow'
        y = 1
    elif index == 2:
        color = 'green'
        g = 1
        
    img.save('../images/' + str(i) + '.png')
    imgs.append(img)
    row = ["/images/" + str(i) + ".png", color, r, y, g]
    train.append(row)
print(train)

df = pd.DataFrame(np.array(train), columns=["Image Path", "Color", "Red", "Yellow", "Green"])
print(df)

with open('data.csv', mode='w') as  data:
    data_writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in train:
        data_writer.writerow([row[0], row[1], row[2], row[3], row[4]]) 
