from utils import readFile

def part1(big_line):
    num_list = []
    num_range_list = []
    symbol_list = []

    for i, char in enumerate(big_line):
        if char.isdigit():
            num_range = [i]
            num = char
            big_line[i] = '.'
            if i == 19599:
                break
            if big_line[i + 1].isdigit():
                num_range.append(i + 1)
                num = num + big_line[i + 1]
                big_line[i + 1] = '.'
                if big_line[i + 2].isdigit():
                    num_range.append(i + 2)
                    num_range_list.append(num_range)
                    num = num + big_line[i + 2]
                    num_list.append(num)
                    big_line[i + 2] = '.'
                else:
                    num_list.append(num)
                    num_range_list.append(num_range)
                    continue
            else:
                num_list.append(num)
                num_range_list.append(num_range)
                continue
        elif char != '.':
            symbol_list.append(i)
        
    engine_part_nums = []
    for symbol in symbol_list:
        for i, r in enumerate(num_range_list):
            if symbol in range(r[0] - 1, r[-1] + 2) or (symbol - 140) in range(r[0] - 1, r[-1] + 2) or (symbol + 140) in range(r[0] - 1, r[-1] + 2):
                engine_part_nums.append(int(num_list[i]))
    
    return sum(engine_part_nums)



lines = readFile("day3")

big_line = ''

for line in lines:
    big_line = big_line + line


print("Part 1: ", part1(list(big_line)))