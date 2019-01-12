import re
from .constants import *

def open_log_file(file_path):
    """Reads the content of a text file and returns it as a string."""
    with open(file_path) as file:
        lines = file.read()
    return lines

def split_games(log_lines):
    """Splits an Quake 3 game log into a list of games."""
    game_pattern = GAME_PATTERN_REGEX
    return re.findall(game_pattern, log_lines)

def get_players(game):
    """Returns a list of players on a given game."""

    #First find all lines on which an user has connected"
    user_connect_pattern = USER_CONNECT_REGEX
    user_connects = re.findall(user_connect_pattern, game)

    player_delimiter = re.compile(USER_DELIMITER_REGEX)
    players = set()
    for user in user_connects:
        players.add(player_delimiter.sub("", user))
    
    return list(players)

def get_player_kills(game, player):
    """Returns the number of kills a player has made on a given game."""
    return len(re.findall(PLAYER_KILL_REGEX.format(player, player), game))

def get_player_suicides(game, player):
    """Returns the number of suicide a player has committed."""
    return len(re.findall(SUICIDE_REGEX.format(player, player), game))

def get_player_world_deaths(game, player):
    """Returns the number of deaths a player has suffered from the world."""
    return len(re.findall(WORLD_DEATHS_REGEX.format(player), game))

def get_total_kills(game, players):
    """Returns a tuple with the game's total kills and player score."""
    total_kills = 0
    player_score = {}

    for player in players:
        player_kills = get_player_kills(game, player)
        player_suicides = get_player_suicides(game, player)
        player_world_deaths = get_player_world_deaths(game, player)
        
        total_kills += (player_kills + player_suicides + player_world_deaths)
        player_score[player] = (player_kills - player_world_deaths)

    return (total_kills, player_score)