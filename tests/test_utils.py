# conding: utf-8

from unittest import TestCase

from tests import UtilsCommand, module


class TestMakeSureDirExists(TestCase):
    dir_path = "tmp/laksjdh"

    def test1(self):
        self.assertFalse(module.os.path.exists(self.dir_path))
        UtilsCommand.call("make_sure_dir_exists", self.dir_path)
        self.assertTrue(module.os.path.isdir(self.dir_path))
        module.shutil.rmtree(self.dir_path)

    def test2(self):
        module.os.mkdir(self.dir_path)
        UtilsCommand.call("make_sure_dir_exists", self.dir_path)
        self.assertTrue(module.os.path.isdir(self.dir_path))
        module.shutil.rmtree(self.dir_path)

    def test3(self):
        open(self.dir_path, "w")
        UtilsCommand.call("make_sure_dir_exists", self.dir_path)
        self.assertTrue(module.os.path.isdir(self.dir_path))
        module.shutil.rmtree(self.dir_path)


class TestMakeSureNotExists(TestCase):
    file_path = "tmp/lqkwehj"

    def test1(self):
        self.assertFalse(module.os.path.exists(self.file_path))
        UtilsCommand.call("make_sure_not_exists", self.file_path)
        self.assertFalse(module.os.path.exists(self.file_path))

    def test2(self):
        open(self.file_path, "w")
        self.assertTrue(module.os.path.exists(self.file_path))
        UtilsCommand.call("make_sure_not_exists", self.file_path)
        self.assertFalse(module.os.path.exists(self.file_path))

    def test3(self):
        module.os.mkdir(self.file_path)
        self.assertTrue(module.os.path.exists(self.file_path))
        UtilsCommand.call("make_sure_not_exists", self.file_path)
        self.assertFalse(module.os.path.exists(self.file_path))


class TestUrlJoin(TestCase):

    def test1(self):
        self.assertEqual(
            UtilsCommand.check_call("path_join", "a", "b"), "a/b",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "a/", "b"), "a/b",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "a", "/b"), "a/b",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "a/", "/b"), "a/b",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "/", "/b"), "/b",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "/", "/"), "/",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "/", ""), "/",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", "", "b"), "/b",
        )
        self.assertEqual(
            UtilsCommand.check_call("path_join", ".", "b"), "./b",
        )


class TestColorPrint(TestCase):

    def test1(self):
        import re
        regex = re.compile(r'\x1b[^m]*m')

        result = UtilsCommand.check_call(
            "color_print", "this\nis\ntest\n",
        )
        self.assertEqual("this\nis\ntest\n", regex.sub('', result))

        result = UtilsCommand.check_call(
            "color_print", "this is test",
            "color=yellow", "mode=bg", "style=underline",
        )
        self.assertEqual("this is test", regex.sub('', result))
