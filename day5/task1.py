def split_data(data:list[str])-> list[list[str]]:
    next_list = False
    first:list[str] = []
    second:list[str] = []
    for d in data:
        if d == "":
            next_list= True
            continue
        if not next_list:
            first.append(d)
        else:
            second.append(d)
    return [first, second]



class Something():
    def __init__(self, rules:list[str]):
        self.rules:list[list[int]] = []
        for r in rules:
            self.rules.append([int(i)for i in r.split("|")])
        print(self.rules)

    def is_allowed(self, int1:int, int2:int):
        for rule in self.rules:
            if rule[0] == int1:
               if rule[1] == int2:
                  return True
        else:
           return False

    def check_entrys(self, data:list[str])-> list[list[int]]:
        good_entrys:list[list[int]] = []
        for entry in data:
            ent = [int(i)for i in entry.split(",")]
            allowed = True
            for i in range(len(ent)-1):
                if not self.is_allowed(ent[i], ent[i+1]):
                    allowed = False
            if allowed:
                good_entrys.append(ent)
        return good_entrys

    def get_middel_numbers(self, data:list[list[int]]):
        middel_numbers:list[int] = []
        for entry in data:
            middel_numbers.append(entry[len(entry)//2])
        return middel_numbers


if __name__ == "__main__":
    with open("day5/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    first, second = split_data(data)
    something = Something(first)
    good_stuff = something.check_entrys(second)
    results = something.get_middel_numbers(good_stuff)
    number = 0
    for r in results:
        number += r
    print(number)
