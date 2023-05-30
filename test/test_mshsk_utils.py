import pathlib
from unittest import TestCase

from mshsk.env import WRAP_OPEN_TAG
from mshsk.mshsk_utils import wrap_single_file


class Test(TestCase):
    TEST_FILE = str(pathlib.Path("resources/index.php").absolute())

    def test_wrap_html_content_success_flow(self):
        wrap_single_file(self.TEST_FILE)

        with open(self.TEST_FILE, mode="r+", encoding="utf-8") as file:
            content = file.read()
            self.assertTrue(WRAP_OPEN_TAG in content)
