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


def count_games(file_name):
    """Returns number of lines in a file (games)"""
    content = open_file(file_name)
    return len(content)


def decide(file_name, year):
    """Returns True if there is a game from given year in a file. Otherwise returns False"""
    if type(year) != int:
        raise ValueError("Not a valid year")
    content = open_file(file_name)
    for game in content:
        if str(year) in game:
            return True
    return False


def get_latest(file_name):
    """Returns title of the latest game in the file"""
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
    return latest[0]


def count_by_genre(file_name, genre):
    """Returns the number of games from given genre from the file"""
    if type(genre) != str:
        raise TypeError("Invalid genre")
    content = open_file(file_name)
    genre_index = 3
    count = 0
    for game in content:
        if genre.lower() == game[genre_index].lower():
            count += 1
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
    return line


def quick_sort(lst):
    """Sorting algorithm"""
    if not lst:
        return []
    return (quick_sort([x for x in lst[1:] if x < lst[0]])
            + [lst[0]] +
            quick_sort([x for x in lst[1:] if x >= lst[0]]))


def sort_abc(file_name):
    """Sort and return title list"""
    content = open_file(file_name)
    title_index = 0
    arr = [game[title_index] for game in content]
    arr = quick_sort(arr)
    return arr


def get_genres(file_name):
    """Return sorted genre list without duplicates"""
    content = open_file(file_name)
    genre_index = 3
    genres = list(set([game[genre_index] for game in content]))
    genres = quick_sort(genres)
    return genres


def when_was_top_sold_fps(file_name):
    """Return year of a top selling fps game"""
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
    return int(best_selling_fps[1])

