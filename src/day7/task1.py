with open("src/day7/data.txt", "r") as f:
# with open("day5/test_data.txt", "r") as f:
    data = f.readlines()
data = [d.strip("\n") for d in data]
equations = []
for line in data:
    test_value, numbers = line.split(":")
    equations.append((int(test_value), [*map(int, numbers.strip().split())]))

result = []

for test_value, numbers in equations:
    possibles = [numbers.pop(0)]
    while numbers:
        curr = numbers.pop(0)
        temp = []
        for p in possibles:
            temp.append(p + curr)
            temp.append(p * curr)
        possibles = temp

    if test_value in possibles:
        result.append(test_value)

print(sum(result))
