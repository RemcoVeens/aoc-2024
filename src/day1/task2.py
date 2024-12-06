from helppers.tools import *

data = load_file("day1/data.txt")
data = [d.split("   ") for d in data]
l1:list[int] =[]
l2:list[int] =[]
sorted_list:list[list[int]] = []
result = 0
for l in data:
    l1.append(int(l[0]))
    l2.append(int(l[1]))
for i in l1:
    c = l2.count(i)
    result += i*c
print(result)
