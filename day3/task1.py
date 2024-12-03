import re

def filter(data:str)->list[str]:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    filtered_string = re.findall(pattern, data)
    return filtered_string

def extract_numbers(data:list[str])->list[list[int]]:
    result:list[list[int]] = []
    for string in data:
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
    print(data)
    # data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    filterd = filter(data)
    results = extract_numbers(filterd)
    result = mathing(results)
    print(result)
