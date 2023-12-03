import re
from utils import readFile

# game = { 'id': 1, 'pull1': {'r': 5, 'g': 7, 'b': 20}, 'pull1': {'r': 4, 'g': 19, 'b': 3} ... }
def parseGame(game):
    gameid = int(re.findall(r'\d+(?=:)', game)[0])
    pulls = game.split(': ')[1]

    parsed_game = { 'id': gameid }

    pull_num = 0
    for pull in pulls.split('; '):
        pull_num += 1
        parsed_game['pull' + str(pull_num)] = {}

        for color_group in pull.split(', '):
            color = re.findall(r'(?<=\ )\w+', color_group)[0]
            count = re.findall(r'\d+(?= )', color_group)
            parsed_game['pull' + str(pull_num)][color[0]] = int(count[0])
    
    return parsed_game



def part1(games):
    game_list = []


    for game in games:
        game = parseGame(game)

        game['valid'] = True

        for pull in game.items():
            if 'pull' in pull[0]:
                for color in pull[1].items():
                    if color[0] == 'r':
                        if color[1] > 12:
                            game['valid'] = False
                    elif color[0] == 'g':
                        if color[1] > 13:
                            game['valid'] = False
                    elif color[0] == 'b':
                        if color[1] > 14:
                            game['valid'] = False
        
        game_list.append(game)
    
    id_sum = 0
    for game in game_list:
        if game['valid'] == True:
            id_sum += game['id']
    
    return id_sum

def part2(games):
    powers = []

    for game in games:
        game = parseGame(game)

        min_red = 0
        min_green = 0
        min_blue = 0
        for pull in game.items():
            if 'pull' in pull[0]:
                if 'r' in pull[1].keys():
                    if pull[1]['r'] > min_red:
                        min_red = pull[1]['r']
                if 'g' in pull[1].keys():
                    if pull[1]['g'] > min_green:
                        min_green = pull[1]['g']
                if 'b' in pull[1].keys():
                    if pull[1]['b'] > min_blue:
                        min_blue = pull[1]['b']
        

        power = min_red * min_green * min_blue
        powers.append(power)
    
    return sum(powers)





# with open("values.txt", 'r') as g:
#     games = [game.rstrip() for game in g.readlines()]

games = readFile("day2")

print("Part 1: ", part1(games), "\nPart 2: ", part2(games))
