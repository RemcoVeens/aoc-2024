import os, sys, glob, re

class PuzzleReader:
    @staticmethod
    def get_puzzle_input(day_num, is_raw):
        return [line.strip("\n") if is_raw else line.strip() for line in open(f"{PuzzleReader.get_path()}/data.txt", "r").readlines()]

    def get_test_input(day_num, is_raw):
        inputs = []
        for name in sorted(glob.glob(f"{PuzzleReader.get_path()}/data/day{day_num:02d}/*")):
            if len(re.findall(r"^test_\d+_input.txt$", os.path.basename(name))):
                inputs += [[line.strip("\n") if is_raw else line.strip() for line in open(name, "r").readlines()]]
        return inputs

    @staticmethod
    def get_test_result(day_num, part_num):
        results = []
        for name in sorted(glob.glob(f"{PuzzleReader.get_path()}/data/day{day_num:02d}/*")):
            if len(re.findall(r"^test_\d+_part" + str(part_num) + "_result.txt$", os.path.basename(name))):
                results += [[line.strip() for line in open(name, "r").readlines()]]
        return results

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

    def part2(self, data):
        safe = 0
        for report in data:
            levels = [*map(int, report.split())]
            if self.is_safe(levels):
                safe += 1
            else:
                for i in range(len(levels)):
                    tolerated_levels = levels[:i] + levels[i + 1 :]
                    if self.is_safe(tolerated_levels):
                        safe += 1
                        break
        return safe

    def is_safe(self, levels):
        differs = [a - b for a, b in zip(levels, levels[1:])]
        is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
        is_in_range = all(0 < abs(i) <= 3 for i in differs)
        if is_monotonic and is_in_range:
            return True
        return False
if __name__ == "__main__":
    with open("day2/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    print(Solution().part2(data=data))
