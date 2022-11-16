#Day 3 - Dart game
import re

"""

"""

file_name = "scores.csv"

def get_names(line_with_names: str) -> list:
    list_with_names = line_with_names.split(",")
    list_with_names_stripped = [name.rstrip() for name in list_with_names] #strips newline character
    return list_with_names_stripped

def get_winning_points(line_with_points: str) -> list:
    points_list = line_with_points.split(",")
    #strips item from non-digits, newline characters and converts to int, also catches empty strings
    for index, points in enumerate(points_list):
        try:
            points_list[index] = int(re.sub('\D', '', points.rstrip()))
        except ValueError:
            points_list[index] = 0
    winning_points_list = points_list
    for index, item in enumerate(winning_points_list):
        try:
            winning_points_list[index] = item
        except ValueError:
            winning_points_list[index] = 0
        if item == max(winning_points_list):
            winning_points_list[index] = 3
        elif item == min(winning_points_list):
            winning_points_list[index] = -1
        else:
            winning_points_list[index] = 0
        if max(winning_points_list) == min(winning_points_list):
            winning_points_list[index] = 0
    return winning_points_list

def get_game_report():
    with open(file_name, encoding="utf-8") as f:
        names_list = get_names(f.readline())
        number_of_players = len(names_list)
        final_points = [0]*number_of_players
        game_report = f'Game report - {number_of_players} players game:\n|'
        for name in names_list:
            game_report += f'{name}|'
        for index, line in enumerate(f, 1): #assumes that line with names is the first line
            round_points = get_winning_points(line)
            game_report += f'\n    Round {index}:\n|'
            for index, points in enumerate(round_points):
                try:
                    final_points[index] += int(points)
                except ValueError:
                    pass
                game_report += f' {points}|'
        game_report += f'\n----------------------------------\n'
        game_report += f'Final report: \n'
        for index, name in enumerate(names_list):
            game_report += f'{name}: {final_points[index]} points\n'
        print(game_report)

get_game_report()

    