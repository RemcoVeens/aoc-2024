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

    def part2(self, data:list[str]):
        blocks, _, space_idx = self.parse_blocks(data)

        curr_block_idx = len(blocks) - 1

        while curr_block_idx > 0:
            if blocks[curr_block_idx].block_type == Block.TYPE_SPACE:
                curr_block_idx -= 1
                continue

            curr_block_len = len(blocks[curr_block_idx].files)
            for curr_space_idx in space_idx:
                if curr_space_idx >= curr_block_idx:
                    break

                if blocks[curr_space_idx].space_length >= curr_block_len:
                    blocks[curr_space_idx].files.extend(blocks[curr_block_idx].files)
                    blocks[curr_space_idx].space_length -= curr_block_len

                    blocks[curr_block_idx].block_type = Block.TYPE_SPACE
                    blocks[curr_block_idx].space_length = curr_block_len
                    blocks[curr_block_idx].files = []

                    if blocks[curr_space_idx].space_length == 0:
                        space_idx.remove(curr_space_idx)

                    break

            curr_block_idx -= 1

        checksum = 0
        pos = 0
        for block in blocks:
            for file in block.files:
                checksum += pos * file
                pos += 1
            if block.block_type == Block.TYPE_SPACE:
                pos += block.space_length

        return checksum


if __name__=="__main__":
    with open("src/day9/data.txt", "r")as f:
    # with open("src/day6/data.txt", "r") as f:
        data = f.readlines()
    data = [d.strip("\n") for d in data]
    result = Solution().part2(data)
    print(result)
