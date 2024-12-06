def part1(data):
    lines = data[:]
    lines.extend(["".join([row[i] for row in data]) for i in range(len(data[0]))])

    def find_diagonals(grid):
        rows, cols = len(grid), len(grid[0])

        # from top-left to bottom-right
        main_diagonals = {}

        # from top-right to bottom-left
        anti_diagonals = {}

        for r in range(rows):
            for c in range(cols):
                key_main = r - c
                if key_main not in main_diagonals:
                    main_diagonals[key_main] = []
                main_diagonals[key_main].append(grid[r][c])

                key_anti = r + c
                if key_anti not in anti_diagonals:
                    anti_diagonals[key_anti] = []
                anti_diagonals[key_anti].append(grid[r][c])

        return main_diagonals, anti_diagonals

    main_diagonals, anti_diagonals = find_diagonals(data)
    lines.extend(["".join(i) for i in main_diagonals.values()])
    lines.extend(["".join(i) for i in anti_diagonals.values()])

    return sum(line.count("XMAS") + line.count("SAMX") for line in lines)


if __name__ == "__main__":
    with open("day4/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    print(part1(data=data))
