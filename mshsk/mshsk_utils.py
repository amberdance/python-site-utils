import html

from bs4 import BeautifulSoup

from exception.ContentWrapException import ContentWrapException
from mshsk.env import *
from util.Files import Files


def wrap_html_content(file_src: any) -> None:
    """
       It only works if php code is present.
       Wraps the html content of the bitrix page in a specified container located between the php open tags <? and ?>
       :param file_src: str
       :rtype: None
       """

    with open(file_src, mode="r+", encoding="utf-8") as file:
        raw_content = file.read()

        if is_content_wrapped(raw_content):
            raise ContentWrapException("Nothing to wrap. Content is already wrapped by: " + WRAP_OPEN_TAG)

        file.truncate(0)  # have to erase file
        file.seek(0)
        file.write(prettify_html(raw_content))
        file.seek(0)

        lines = file.readlines()
        Files.backup_file(file.name, BACKUP_FILENAME_POSTFIX)
        php_tags = find_php_occurrences(lines)

        process_wrap(lines, php_tags)

        file.seek(0)
        file.writelines(lines)


# todo
def delete_wrapping(file_src: any) -> None:
    with open(file_src, mode="r+", encoding="utf-8") as file:
        lines = file.readlines()
        php_tags = find_php_occurrences(lines)

        # process_delete_wrap(lines, php_tags)
        file.seek(0)
        file.writelines(lines)


def prettify_html(content: str) -> str:
    content = re.sub("<\?(?!php)", "<?php ", content)
    soup = BeautifulSoup(content, "html.parser").prettify()

    return html.unescape(soup)


def is_content_wrapped(content: str) -> bool:
    return WRAP_OPEN_TAG in content


def find_php_occurrences(lines: list):
    result = []

    for (position, line) in enumerate(lines):
        if PHP_CLOSE_TAG in line:
            result.append([position, line])

    return result


def process_wrap(lines: list, php_tag_occurrences: list) -> None:
    html_ends_line = php_tag_occurrences[-1][0]  # position where last php close tag occur
    lines.insert(html_ends_line, WRAP_CLOSE_TAG + "\n" * COUNT_OF_BLANK_LINES)

    html_starts_line = php_tag_occurrences[0][0]  # position where first php close tag occur
    del lines[html_starts_line]

    lines.insert(html_starts_line, PHP_CLOSE_TAG + "\n" * COUNT_OF_BLANK_LINES)
    lines.insert(html_starts_line + line_insert_index, WRAP_OPEN_TAG + "\n")

    content_after_php_close_tag = re.search(php_close_tag_pattern, php_tag_occurrences[0][1])

    if content_after_php_close_tag is not None and content_after_php_close_tag[0] != "":
        lines.insert(html_starts_line + line_insert_index + 1, content_after_php_close_tag[0])
