import matplotlib.pyplot as plt
import json
from math import dist
from random import shuffle, choice
X = 0
Y = 1
pause_interval = 0.05
num_of_cities = 10
GENERATION = num_of_cities * 10
xmin, ymin, xmax, ymax = -100, -100, 100, 100
plt.axis([xmin, xmax, ymin, ymax])
labels = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
cities_json = {}

def generateCityName(N):
    name = ""
    copylabels = labels
    for _ in range(N):
        char = choice(copylabels)
        name += char
        copylabels.remove(char)

    return name

def getData(file_name = ""):
    
    if file_name != "":

        with open(file_name) as fi:

            cities_json = json.load(fi)

        cities = [ city['name'] for city in cities_json['cities']]
        x_cities = [ city['x_coord'] for city in cities_json['cities']]
        y_cities = [ city['y_coord'] for city in cities_json['cities']]
        for i in range(len(cities)):
            print(f"City : {cities[i]} ({x_cities[i]},{y_cities[i]})")
    else:
        len_char_set = len(labels)
        city_chars = int(num_of_cities / len_char_set) + 1
        cities = [generateCityName(city_chars) for _ in range(num_of_cities)]
        x_cities = [int(choice(list(range(xmin, xmax)))) for _ in range(num_of_cities)]
        y_cities = [int(choice(list(range(ymin, ymax)))) for _ in range(num_of_cities)]
        
    return x_cities, y_cities, cities

def getDistance(x, y):
    
    distance = 0
    for i in range(len(x) - 1):
        distance += dist([x[i], y[i]], [x[i+1], y[i+1]])
    return distance


def rearrange(x_cities, y_cities, cities):

    temp = list(zip(x_cities, y_cities, cities))
    shuffle(temp)
    x, y, c = zip(*temp)
    x = list(x)
    y = list(y)
    c = list(c)
    
    x.append(x[0])
    y.append(y[0])
    c.append(c[0])

    return x,y,c

if __name__ == "__main__":

    x_cities, y_cities, cities =  getData()
    x_best , y_best, c_best = x_cities , y_cities, cities
    shortest_distance = getDistance(x_best, y_best)
    
    for i in range(GENERATION):
        plt.subplot(1,2,1)
        plt.plot(x_cities, y_cities, 'red')

        plt.subplot(1,2,2)
        plt.plot(x_best, y_best, 'green')

        plt.pause(pause_interval)
        plt.clf()
        x_cities, y_cities, cities = rearrange(x_cities[:-1], y_cities[:-1], cities[:-1])
        distance = getDistance(x_cities, y_cities)

        print(f"Generation {(i+1)}/{GENERATION} Distance : {round(distance, 4)} \tShortest : {round(shortest_distance, 4)}\tOrder : {c_best}")
        
        if distance < shortest_distance:
            x_best, y_best, c_best = x_cities, y_cities, cities
            shortest_distance = distance
        plt.plot(x_best, y_best, 'green')

    plt.show()