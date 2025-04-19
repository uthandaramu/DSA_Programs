import csv

with open('data/nyc_weather.csv', 'r') as f:
    data_array=[]
    reader = csv.reader(f)
    for row in reader:
        try:
            data_array.append(int(row[1]))
        except:
            print("Invalid data ignored")
print(data_array)
print("Average temp of first week of Jan: ", sum(data_array[0:7])/7)
print("Max temperature in 10 days: ", max(data_array[:10]))