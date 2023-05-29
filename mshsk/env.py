import re

PHP_CLOSE_TAG = "?>"
WRAP_OPEN_TAG = "<div class='container'>"
WRAP_CLOSE_TAG = "</div>"
COUNT_OF_BLANK_LINES = 2
BACKUP_FILENAME_POSTFIX = "hrd2cd.bak"

php_close_tag_pattern = re.compile("(?<=\?>).*")
line_insert_index = 1
