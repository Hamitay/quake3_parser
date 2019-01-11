#REGEXES
MATCH_PATTERN_REGEX = r"(InitGame:[.\s\S]*?ShutdownGame:)"
USER_CONNECT_REGEX = r"ClientUserinfoChanged:.*?\\t"
USER_DELIMITER_REGEX = r"(ClientUserinfoChanged:(.)*?n\\)|(\\t)"
