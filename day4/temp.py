import os
import sys
class PuzzleReader:
    @staticmethod
    def get_puzzle_input(day_num, is_raw):
        return [line.strip("\n") if is_raw else line.strip() for line in open(f"{PuzzleReader.get_path()}/data.txt", "r").readlines()]

    @staticmethod
    def get_path():
        return path if os.path.isdir(path := os.path.realpath(sys.argv[0])) else os.path.dirname(path)
class SolutionBase:
    def __init__(self, day_num: int = -1, is_raw: bool = False, skip_test: bool = False, benchmark: bool = False):
        self.day_num = day_num
        self.is_raw = is_raw
        self.skip_test = skip_test
        self._benchmark = benchmark
        self.benchmark_times = []
        self.data = PuzzleReader.get_puzzle_input(self.day_num, self.is_raw)

class Solution(SolutionBase):
    def part1(self, data):
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

    def part2(self, data):
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
    print(Solution().part2(data=data))
