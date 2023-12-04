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

    f = open("./day02/day02_part01_input.txt", 'r')

    games_dict = {}
    game_products = []

    for line in f.readlines():
        game, scores = line.strip().split(':')
        game_id = get_game_id(game)
        sub_games = get_sub_game_list(scores)
        games_dict[game_id] = sub_games



    for game_id, sub_games in games_dict.items():

        # Get the maximum number of cubes per colour per sub-game, hold onto the max per game
        max_cubes = {'red': 0,
                     'green': 0,
                     'blue': 0}

        print ("game: ", game_id)

        for sub_game in sub_games:      # e.g. {'green': 5, 'blue': 11, 'red': 6}
            for colour in sub_game.keys():
                if sub_game[colour] > max_cubes[colour]:
                    max_cubes[colour] = sub_game[colour]

        game_product = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
        game_products.append(game_product)

    answer = sum(game_products)
    print(answer)
