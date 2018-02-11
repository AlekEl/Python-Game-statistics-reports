
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


def quick_sort(lst):
    """Sorting algorithm"""
    if not lst:
        return []
    return (quick_sort([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quick_sort([x for x in lst[1:] if x >= lst[0]]))


def sort_abc(file_name):
    """Sort, print and return title list"""
    content = open_file(file_name)
    title_index = 0
    arr = [game[title_index] for game in content]
    arr = quick_sort(arr)
    print("Sorted title list: {0}".format(arr))
    return arr


def get_genres(file_name):
    """Return and print sorted genre list without duplicates"""
    content = open_file(file_name)
    genre_index = 3
    genres = list(set([game[genre_index] for game in content]))
    genres = quick_sort(genres)
    print("Genre list: {0}".format(genres))
    return genres


def when_was_top_sold_fps(file_name):
    """Return nad print year of a top selling fps game"""
    content = open_file(file_name)
    copies_sold_index = 1
    year_index = 2
    genre_index = 3
    best_selling_fps = []
    for game in content:
        if game[genre_index] == "First-person shooter":
            if len(best_selling_fps) == 0:
                best_selling_fps = [float(game[copies_sold_index]), game[year_index]]
            elif best_selling_fps[0] < float(game[copies_sold_index]):
                best_selling_fps = [float(game[copies_sold_index]), game[year_index]]
    if len(best_selling_fps) == 0:
        raise ValueError("No fps game in the file")
    print("Release date of best selling fps: {0}".format(int(best_selling_fps[1])))
    return int(best_selling_fps[1])


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
                 get_line_number_by_title(file_name, title),
                 sort_abc(file_name),
                 get_genres(file_name),
                 when_was_top_sold_fps(file_name)]
    for answer in functions:
        answer


print_answers("game_stat.txt")