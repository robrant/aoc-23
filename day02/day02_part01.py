import re

def get_game_id(game_text: str) -> int:
    """ Gets the game ID from the game_text """

    matches = re.search(r'Game (\d+)', game_text)
    game_id = int(matches.groups()[0])
    return game_id

def get_sub_game_list(scores: str) -> int:
    """ Creates a list based on the sub-game score text"""

    sub_games_list = []
    sub_games = scores.split(';')
    for sub_game in sub_games:
        d = {}
        for colour_count in sub_game.split(','):
            colour_count = colour_count.strip()
            matches = re.search(r'(\d+) (green|blue|red)', colour_count)
            m = matches.groups()
            d[m[1]] = int(m[0])
        sub_games_list.append(d)

    return sub_games_list

if __name__ == '__main__':

    # 12 red cubes, 13 green cubes, and 14 blue cubes
    max_cubes = {'red': 12,
                 'green': 13,
                 'blue': 14}

    f = open("./day02/day02_part01_input.txt", 'r')

    games_dict = {}
    impossible_games = []
    possible_games = []

    for line in f.readlines():
        game, scores = line.strip().split(':')
        game_id = get_game_id(game)
        sub_games = get_sub_game_list(scores)
        games_dict[game_id] = sub_games

    for game_id, sub_games in games_dict.items():
        
        break_out_flag = False
        for sub_game in sub_games:      # e.g. {'green': 5, 'blue': 11, 'red': 6}
            for colour in sub_game.keys():
                if sub_game[colour] > max_cubes[colour]:
                    impossible_games.append(game_id)
                    break_out_flag = True
                    break
            if break_out_flag:
                print (game_id, sub_games)
                break

    for game_id in games_dict.keys():
        if not game_id in impossible_games:
            possible_games.append(game_id)

    print (impossible_games)
    print (sum(possible_games))


