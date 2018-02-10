
# Report functions


def open_file(file_name):
    """Opens the file and returns content in form of a list"""
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
            content = [game for game in content if game]
            content = [game.split("\t") for game in content]
            return content
    except FileNotFoundError as err:
        raise err


def get_most_played(file_name):
    """Return best selling game from the file"""
    content = open_file(file_name)
    game_name = content[0][0]
    copies_sold = int(content[0][1])
    best_selling_game = [game_name, copies_sold]
    for game in range(1, len(content)):
        game_name = content[game][0]
        copies_sold = int(content[game][2])
        if best_selling_game[1] < copies_sold:
            best_selling_game[0] = game_name
            best_selling_game[1] = copies_sold
    return best_selling_game[0]


def sum_sold(file_name):
    """Return sum of sold copies of all the games from the file"""
    content = open_file(file_name)
    copies_sold_index = 1
    sum_of_copies_sold = 0
    for game in content:
        sum_of_copies_sold += float(game[copies_sold_index])
    return sum_of_copies_sold


def get_selling_avg(file_name):
    """Return average number of sold copies from all the games from file"""
    content = open_file(file_name)
    avg = sum_sold(file_name)/len(content)
    return avg


def count_longest_title(file_name):
    """Return number of characters in longest game title from the file"""
    content = open_file(file_name)
    title_index = 0
    longest_title = len(content[0][title_index])
    for game in range(1, len(content)):
        if longest_title < len(content[game][title_index]):
            longest_title = len(content[game][title_index])
    return longest_title


def get_date_avg(file_name):
    """Return average release date of all games from the file"""
    content = open_file(file_name)
    year_index = 2
    sum_of_release_dates = 0
    for game in content:
        sum_of_release_dates += float(game[year_index])
    avg = int(sum_of_release_dates / len(content)) + (sum_of_release_dates % len(content) > 0)
    return avg


def get_game(file_name, title):
    """Return properties of a given game"""
    content = open_file(file_name)
    game_properties = []
    title_index = 0
    copies_sold_index = 1
    release_date_index = 2
    for games in range(len(content)):
        for game in range(len(content[games])):
            if title.lower() == content[games][title_index].lower():
                if game == copies_sold_index:
                    game_properties.append(float(content[games][copies_sold_index]))
                elif game == release_date_index:
                    game_properties.append(int(content[games][release_date_index]))
                else:
                    content[games][game] = content[games][game].replace("\n", "")
                    game_properties.append(content[games][game])
    return game_properties
