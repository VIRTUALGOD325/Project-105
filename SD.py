import pandas as pd 
import csv
import math 

file = open("data.csv","r")

reader = csv.reader(file)

file_data = list(reader)

file_data.pop(0)

numbers = []

for row in range(len(file_data)):
    num = file_data[row][0]
    numbers.append(float(num))

total = 0

for i in numbers:
    total += i

mean_value = total/len(numbers)
print(mean_value)

data_frame = pd.read_csv('data.csv')

sqrd_diff = []

for num in numbers:
    diff = int(num) - mean_value 
    diff = diff**2 
    sqrd_diff.append(diff)

sum = 0

for i in sqrd_diff:
    sum = sum + i

result = sum/len(numbers)

SD = math.sqrt(result)
print(SD)