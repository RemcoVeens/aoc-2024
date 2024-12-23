from dataclasses import dataclass


@dataclass
class Block:
    block_type: int
    files: list[int]
    space_length: int

    TYPE_FILE = 1
    TYPE_SPACE = 0


class Solution:
    def parse_blocks(self, data:list[str]):
        disk_map = data[0]
        blocks:list[Block] = []  # [block_type, [file_id], space_length]

        block_type = Block.TYPE_FILE  # 0: space, 1: file
        file_id = 0
        space_count = 0
        space_idx:list[int] = []

        for i in map(int, disk_map):
            if block_type == Block.TYPE_FILE:
                block = Block(
                    block_type=block_type,
                    files=[file_id] * i,
                    space_length=0,
                )
                blocks.append(block)
                file_id += 1
            else:
                if i > 0:
                    space_count += i
                    space_idx.append(len(blocks))
                    block = Block(
                        block_type=block_type,
                        files=[],
                        space_length=i,
                    )
                    blocks.append(block)
            block_type = (block_type + 1) % 2

        return blocks, space_count, space_idx

    def part1(self, data:list[str]):
        blocks, space_count, space_idx = self.parse_blocks(data)

        curr_block = []
        curr_space_idx = space_idx.pop(0)

        while space_count:
            if len(curr_block) == 0:
                if blocks[-1].block_type == Block.TYPE_SPACE and len(blocks[-1].files) == 0:
                    blocks.pop()
                    space_idx.pop()
                    continue

                if blocks[-1].block_type == Block.TYPE_FILE:
                    curr_block = blocks.pop().files

            try:
                item = curr_block.pop()
            except IndexError:
                break

            blocks[curr_space_idx].files.append(item)
            blocks[curr_space_idx].space_length -= 1
            space_count -= 1

            if blocks[curr_space_idx].space_length == 0:
                blocks[curr_space_idx].block_type = 1
                if space_idx:
                    curr_space_idx = space_idx.pop(0)
                else:
                    break

        if curr_block:
            blocks.append(
                Block(
                    block_type=Block.TYPE_FILE,
                    files=curr_block,
                    space_length=0,
                )
            )
        checksum = 0
        pos = 0
        for block in blocks:
            for file in block.files:
                checksum += pos * file
                pos += 1

        return checksum


if __name__=="__main__":
    with open("src/day9/data.txt", "r")as f:
    # with open("src/day6/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    result = Solution().part1(data)
    print(result)
