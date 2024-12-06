def part2(data):
    rows, cols = len(data), len(data[0])
    count = 0

    _set = {"M", "S"}

    # find A as center of the cross, then check the diagonals
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == "A":
                if {data[r - 1][c - 1], data[r + 1][c + 1]} == _set and {data[r - 1][c + 1], data[r + 1][c - 1]} == _set:
                    count += 1

    return count

if __name__ == "__main__":
    with open("day4/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    print(part2(data=data))
