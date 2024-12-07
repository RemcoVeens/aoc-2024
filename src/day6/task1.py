import os

class Guard:
    def __init__(self, current_pos:list[int]):
        self.current_pos = current_pos
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
            self.new_pos = [self.current_pos[0]-1, self.current_pos[1]]
        elif self.facing == "RIGHT":
            self.new_pos = [self.current_pos[0], self.current_pos[1]+1]
        elif self.facing == "DOWN":
            self.new_pos = [self.current_pos[0]+1, self.current_pos[1]]
        else:
            self.new_pos = [self.current_pos[0], self.current_pos[1]-1]
        return self.new_pos



class GuardGame:
    def __init__(self, map:list[str]):
        self.map:list[list[str]] = []
        for row in map:
            row_map:list[str] = []
            for c in row:
                row_map.append(c)
            self.map.append(row_map)
        self.guard = Guard(current_pos=self.find_guard_pos())
        self.good_spot = [".","X"]

    def find_guard_pos(self)->list[int]:
        for i,row in enumerate(self.map):
            for j, c in enumerate(row):
                if c =="^":
                    return [i,j]
        else:
            raise Exception("Guard now found")

    def show_map(self):
        os.system("clear") # clear for nice game effect
        for row in self.map:
            for c in row:
                print(c, end="")
            print()

    def what_is_cord(self, cord:list[int])->str:
        return self.map[cord[0]][cord[1]]

    def is_edge(self, cord:list[int])->bool:
        x,y = cord
        if x <0 or y <0:
            # left or top edge
            return True
        if x>=len(self.map) or y>=len(self.map[0]):
            # right or bottem edge
            return True
        return False

    def count(self)->int:
        c= 0
        for row in self.map:
            for i in row:
                if i == "X":
                    c += 1
        return c


    # TODO:
        # if next spot is "#", turn, recal new pos
        # move to new spot if "." or "X"
        # replace old pos with "X"
        # if next pos is off map: count "X""
    def main(self)->int:
        while True:
            self.show_map()
            ns = self.guard.next_spot()
            if self.is_edge(ns):
                self.map[self.guard.current_pos[0]][self.guard.current_pos[1]] = "X"
                break
            if self.what_is_cord(ns) in self.good_spot:
                self.map[self.guard.current_pos[0]][self.guard.current_pos[1]] = "X"
                self.map[self.guard.new_pos[0]][self.guard.new_pos[1]] = "^"
                self.guard.current_pos = self.guard.new_pos
            else:
                self.guard.rotate()
        return self.count()




if __name__=="__main__":
    with open("src/day6/data.txt", "r")as f:
    # with open("src/day6/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    gg =GuardGame(data)
    print(gg.main())
