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
for i1, i2 in zip(sorted(l1),sorted(l2)):
   sorted_list.append([i1,i2])
# print(sorted_list)
for ints in sorted_list:
    result += abs(ints[0]-ints[1])
print(result)
