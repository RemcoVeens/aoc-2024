import os

class Guard:
    def __init__(self, current_pos:list[int]):
        self.current_pos = current_pos
        print(self.current_pos)
        self.facing:str="UP"

    def rotate(self):
        if self.facing == "UP":
            self.facing = "RIGHT"
        elif self.facing == "RIGHT":
            self.facing = "DOWN"
        elif self.facing == "DOWN":
            self.facing = "LEFT"
        else:
            self.facing = "UP"

    def next_spot(self)->list[int]:
        if self.facing == "UP":
            self.new_pos = [self.current_pos[0]+1, self.current_pos[1]]
        elif self.facing == "RIGHT":
            self.new_pos = [self.current_pos[0], self.current_pos[1]+1]
        elif self.facing == "DOWN":
            self.new_pos = [self.current_pos[0]-1, self.current_pos[1]]
        else:
            self.new_pos = [self.current_pos[0], self.current_pos[1]-1]
        return self.new_pos



class GuardGame:
    def __init__(self, map:list[str]):
        self.map:list[list[str]] = []
        for row in map:
            row_map = []
            for c in row:
                row_map.append(c)
            self.map.append(row_map)
        self.guard = Guard(current_pos=self.find_guard_pos())

    def find_guard_pos(self)->list[int]:
        for i,row in enumerate(self.map):
            for j, c in enumerate(row):
                if c =="^":
                    return [i,j]
        else:
            raise Exception("guard now found")

    def show_map(self):
        os.system("clear") # clear for nice game effect
        for row in self.map:
            for c in row:
                print(c, end="")
            print()

    # TODO:
        # if next spot is "#", turn, recal new pos
        # move to new spot if "." or "X"
        # replace old pos with "X"
        # if next pos is off map: count "X""


if __name__=="__main__":
    with open("src/day6/test_data.txt", "r")as f:
    # with open("src/day6/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    gg =GuardGame(data)
    gg.show_map()
