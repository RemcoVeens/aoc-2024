import re

def filter(data:str)->list[str]:
    pattern = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
    filtered_string = re.findall(pattern, data)
    result:list[str] = []
    for tub in filtered_string:
        for i in range(3):
            if tub[i]!='':
                result.append(tub[i])
    return result

def extract_numbers(data:list[str])->list[list[int]]:
    result:list[list[int]] = []
    active = True
    for string in data:
        if string =="don't()":
            active =False
            continue
        elif string == "do()":
            active =True
            continue
        else:
            if active:
                p1 = string.split("(")[1].split(")")[0]
                ints = [int(i) for i in p1.split(",")]
                result.append(ints)
    return result

def mathing(data:list[list[int]])-> int:
    result = 0
    for i in data:
        result += int(i[0]*i[1])
    return result

if __name__ == "__main__":
    with open("day3/data.txt", "r") as f:
        data = f.readlines()
    data = "".join(data)
    filterd = filter(data)
    results = extract_numbers(filterd)
    result = mathing(results)
    print(result)
