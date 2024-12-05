import random
import numpy as np
from tqdm import tqdm

from collections import defaultdict


class AoC():
    def extract_data(self, data):
        _sep = data.index("")

        self.rules = defaultdict(set)
        for i in data[:_sep]:
            a, b = map(int, i.split("|"))
            self.rules[a].add(b)

        self.updates = [list(map(int, i.split(","))) for i in data[_sep + 1 :]]

    def is_valid(self, update):
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] not in self.rules[update[i]]:
                    return False
        return True

    def fix_update(self, update):
        filtered_rules = defaultdict(set)
        for i in update:
            filtered_rules[i] = self.rules[i] & set(update)

        # ordered_items = sorted(filtered_rules.items(), key=lambda x: len(x[1]), reverse=True)
        # ordered_keys = [i[0] for i in ordered_items]
        ordered_keys = sorted(filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True)

        return ordered_keys

    def part2(self, data):
        self.extract_data(data)
        add_up = 0

        for update in self.updates:
            if not self.is_valid(update):
                fixed_update = self.fix_update(update)
                add_up += fixed_update[len(update) // 2]

        return add_up
if __name__ == "__main__":
    with open("day5/data.txt", "r") as f:
    # with open("day5/test_data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    print(AoC().part2(data=data))
