import csv
with open ('123.csv') as a:
    read = csv.reader(a)
    data = list(read)

data.pop(0)
new_data = []
for b in range(len(data)):
    c = data[b][1]
    new_data.append(float(c))

n = len(new_data)
new_data.sort()
if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1]) 
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
print("Median:"+str(median))