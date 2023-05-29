import os
import pathlib
from unittest import TestCase

from util.Files import Files


class TestFiles(TestCase):
    TEST_FILE = str(pathlib.Path("resources/index.php").absolute())

    def test_path(self):
        self.assertEqual(self.TEST_FILE, str(Files.path(self.TEST_FILE)))

    def test_backup_file(self):
        file = Files.backup_file(self.TEST_FILE, "test.bak")
        self.assertTrue(pathlib.Path(file).exists())
        self.assertEqual(os.path.getsize(file), os.path.getsize(self.TEST_FILE))
        pathlib.Path(file).unlink()

    def test_get_file_extension(self):
        self.assertEqual(Files.get_file_extension(self.TEST_FILE), ".php")

    def test_get_root_directory(self):
        self.assertEqual(os.getcwd(), Files.get_root_directory())
