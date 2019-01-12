#REGEXES PATTERNS
GAME_PATTERN_REGEX = r"(InitGame:[.\s\S]*?ShutdownGame:)"
USER_CONNECT_REGEX = r"ClientUserinfoChanged:.*?\\t"
USER_DELIMITER_REGEX = r"(ClientUserinfoChanged:(.)*?n\\)|(\\t)"
PLAYER_KILL_REGEX = r"{} killed ((?!{}).*) by"
SUICIDE_REGEX = r"{} killed {} by"
WORLD_DEATHS_REGEX = r"<world> killed {} by"

#OUTPUT KEYS
KILLS_KEY = "kills"
TOTAL_KILLS_KEY = "total_kills"
PLAYER_KEY = "players"
GAME_KEY_PATTERN = "game_{}"

