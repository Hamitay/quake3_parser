import re
from .constants import *

def open_log_file(file_path):
    """Reads the content of a text file and returns it as a string."""
    with open(file_path) as file:
        lines = file.read()
    return lines

def split_games(log_lines):
    """Splits an Quake 3 game log into a list of matches."""
    match_pattern = MATCH_PATTERN_REGEX
    return re.findall(match_pattern, log_lines)

def get_players(match):
    """Returns a list of players on a given match."""

    #First find all lines on which an user has connected"
    user_connect_pattern = USER_CONNECT_REGEX
    user_connects = re.findall(user_connect_pattern, match)

    player_delimiter = re.compile(USER_DELIMITER_REGEX)
    players = set()
    for user in user_connects:
        players.add(player_delimiter.sub("", user))
    
    return list(players)
