
def load_and_sort()-> list[list[str]]:
    with open("day4/data.txt","r")as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    formated = []
    for row in data:
        temp= []
        for c in row:
            temp.append(c)
        formated.append(temp)
    return formated

def get_x_cords(data:list[list[str]])->list[list[int]]:
    result = []
    for i, row in enumerate(data):
        for j ,char in enumerate(row):
            if char =="X":
                result.append([i,j])
    return result

def get_word_all_dirs(data:list[list[str]], x_cords:list[list[int]]) -> list[list[str]]:
    all_words = []
    for x_pos in x_cords:
        words = []
        try:
            # horizontal +
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]][x_pos[1]+1],data[x_pos[0]][x_pos[1]+2],data[x_pos[0]][x_pos[1]+3]])
        except IndexError:
            pass
        try:
            # horizontal -
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]][x_pos[1]-1],data[x_pos[0]][x_pos[1]-2],data[x_pos[0]][x_pos[1]-3]])
        except IndexError:
            pass
        try:
            #vertical +
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]+1][x_pos[1]],data[x_pos[0]+2][x_pos[1]],data[x_pos[0]+3][x_pos[1]]])
        except IndexError:
            pass
        try:
            #vertical -
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]-1][x_pos[1]],data[x_pos[0]-2][x_pos[1]],data[x_pos[0]-3][x_pos[1]]])
        except IndexError:
            pass
        try:
            #diagonal + +
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]+1][x_pos[1]+1],data[x_pos[0]+2][x_pos[1]+2],data[x_pos[0]+3][x_pos[1]+3]])
        except IndexError:
            pass
        # try:
        #     #diagonal + -
        #     words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]+1][x_pos[1]-1],data[x_pos[0]+2][x_pos[1]-2],data[x_pos[0]+3][x_pos[1]-3]])
        # except IndexError:
        #     pass
        try:
            #diagonal - +
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]-1][x_pos[1]+1],data[x_pos[0]-2][x_pos[1]+2],data[x_pos[0]-3][x_pos[1]+3]])
        except IndexError:
            pass
        try:
            #diagonal - -
            words.append([data[x_pos[0]][x_pos[1]],data[x_pos[0]-1][x_pos[1]-1],data[x_pos[0]-2][x_pos[1]-2],data[x_pos[0]-3][x_pos[1]-3]])
        except IndexError:
            pass
        all_words.append(words)
    return all_words

def count_xmas(words:list[list[str]]) -> int:
    count = 0
    for word in words:
        for w in word:
            if w == ["X","M","A","S"]:
                print(w)
                count+=1
    return count

if __name__ == "__main__":
    data = load_and_sort()
    x_cords = get_x_cords(data)
    for i in x_cords:
        assert data[i[0]][i[1]] =="X"
    words = get_word_all_dirs(data, x_cords)
    count = count_xmas(words)
    print(count)
