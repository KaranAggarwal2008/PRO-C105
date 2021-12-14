import math
import csv
with open('data.csv', newline='') as frameObject:
    reader = csv.reader(frameObject)
    file_data = list(reader)


data = file_data[0]

def mean(data):
    numberOFValues= len(data)
    total =0
    for eachValue in data:
        total += int(eachValue)

    mean = total / numberOFValues
    return mean



squared_list= []
for EachNumber in data:
    answer=int(EachNumber)-mean(data)
    answer=answer**2
    squared_list.append(answer)


sum =0
for eachSquaredNumber in squared_list:
    sum =sum + eachSquaredNumber

result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)
