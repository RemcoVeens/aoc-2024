with open("day2/data.txt", "r") as f:
    data = f.readlines()
data = [d.strip("\n") for d in data]
data = [d.split(" ") for d in data]
formated:list[list[int]] = []
safe_count = 0
for row in data:
    formated.append([int(i) for i in row])
for row in formated:
    bigger:list[bool] =[]
    smaller:list[bool] = []
    for i in range(len(row)-1):
        if abs(row[i]- row[i+1]) not in [1,2,3]:
            break
        smaller.append(row[i]>row[i+1])
        bigger.append(row[i]<row[i+1])
    else:
        print(row, all(smaller), all(bigger))
        if all(smaller) or all(bigger):
            safe_count+=1
print(safe_count)
