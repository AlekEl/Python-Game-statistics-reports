
# Printing functions


def open_file(file_name):
    """Open the file and return content in form of a list"""
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
            content = [game for game in content if game]
            content = [game.split("\t") for game in content]
            return content
    except FileNotFoundError as err:
        raise err


def count_games(file_name):
    """Return and print number of lines in a file (games)"""
    content = open_file(file_name)
    print("Number of games in the file:", len(content))
    return len(content)


def decide(file_name, year):
    """Return and print True if there is a game from given year in a file. Otherwise returns False"""
    if type(year) != int:
        raise ValueError("Not a valid year")
    content = open_file(file_name)
    for game in content:
        if str(year) in game:
            print("There is a game from {0} in the file".format(year))
            return True
    print("There is no game from {0} in the file".format(year))
    return False


def get_latest(file_name):
    """Return and print title of the latest game in the file"""
    content = open_file(file_name)
    game_name = content[0][0]
    game_year = int(content[0][2])
    latest = [game_name, game_year]
    for game in range(1, len(content)):
        game_name = content[game][0]
        game_year = int(content[game][2])
        if latest[1] < game_year:
            latest[0] = game_name
            latest[1] = game_year
    print("Latest game from the file:", latest[0])
    return latest[0]


def count_by_genre(file_name, genre):
    """Return and print the number of games from given genre from the file"""
    if type(genre) != str:
        raise TypeError("Invalid genre")
    content = open_file(file_name)
    genre_index = 3
    count = 0
    for game in content:
        if genre.lower() == game[genre_index].lower():
            count += 1
    if count > 1:
        print("There are {0} {1}s in the file".format(count, genre))
    elif count == 1:
        print("There is one {0} in the file".format(genre))
    else:
        print("There are no {0} in the file".format(genre))
    return count


def get_line_number_by_title(file_name, title):
    """Returns the number of line of a given game(title) from the file"""
    if type(title) != str:
        raise TypeError("Invalid title")
    content = open_file(file_name)
    title_index = 0
    titles = [game[title_index] for game in content]
    try:
        line = titles.index(title) + 1
    except ValueError as err:
        raise err
    print("{0} is on the {1} line of the file".format(title, line))
    return line


def print_answers(file_name):
    try:
        year = int(input("Year of the game: "))
    except ValueError as err:
        raise err
    genre = input("Genre of the game: ")
    title = input("Title of the game: ")
    functions = [count_games(file_name),
                 decide(file_name, year),
                 get_latest(file_name),
                 count_by_genre(file_name, genre),
                 get_line_number_by_title(file_name, title)]
    for answer in functions:
        answer


print_answers("game_stat.txt")