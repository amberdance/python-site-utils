import os

from mshsk.mshsk_utils import wrap_html_content
from util.Files import Files

if __name__ == '__main__':
    wrap_html_content(Files.path("resources/index.php"))
