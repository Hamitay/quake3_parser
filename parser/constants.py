#REGEXES
GAME_PATTERN_REGEX = r"(InitGame:[.\s\S]*?ShutdownGame:)"
USER_CONNECT_REGEX = r"ClientUserinfoChanged:.*?\\t"
USER_DELIMITER_REGEX = r"(ClientUserinfoChanged:(.)*?n\\)|(\\t)"
PLAYER_KILL_REGEX = r"{} killed ((?!{}).*) by"
SUICIDE_REGEX = r"{} killed {} by"
WORLD_DEATHS_REGEX = r"<world> killed {} by"
