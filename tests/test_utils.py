# conding: utf-8

from unittest import TestCase

from tests import UtilsCommand, module, CommandError

# region functional


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

# end functional

# region filesystem


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


class TestMakeSureParentDirExists(TestCase):
    dir_path = "tmp/mbnzxrw"

    def setUp(self):
        if module.os.path.exists(self.dir_path):
            module.shutil.rmtree(self.dir_path)

    def tearDown(self):
        if module.os.path.exists(self.dir_path):
            module.shutil.rmtree(self.dir_path)

    def test1(self):
        self.assertFalse(module.os.path.exists(self.dir_path))
        UtilsCommand.check_call(
            "make_sure_parent_dir_exists", self.dir_path + "/test",
        )
        self.assertTrue(module.os.path.isdir(self.dir_path))
        UtilsCommand.check_call(
            "make_sure_parent_dir_exists", self.dir_path + "/test1",
        )
        self.assertTrue(module.os.path.isdir(self.dir_path))

    def test2(self):
        self.assertFalse(module.os.path.exists(self.dir_path))
        UtilsCommand.check_call(
            "make_sure_parent_dir_exists", self.dir_path + "/test1/test2",
        )
        self.assertTrue(module.os.path.exists(self.dir_path))
        self.assertTrue(module.os.path.exists(self.dir_path + "/test1"))


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

# end filesystem

# region file


class TestIsStrInFile(TestCase):

    def setUp(self):
        self.fp = module.tempfile.NamedTemporaryFile()
        self.fp.write(b'This is a test\ntest success\nwow')
        self.fp.flush()

    def tearDown(self):
        self.fp.close()

    def test1(self):
        result = UtilsCommand.call("is_str_in_file", "success", self.fp.name)
        self.assertEqual(result.code, 0)

        with self.assertRaises(CommandError):
            try:
                UtilsCommand.call("is_str_in_file", "fail", self.fp.name)
            except CommandError as error:
                self.assertNotEqual(error.result.code, 0)
                self.assertEqual(error.result.stderr, "")
                raise

    def test2(self):
        with self.assertRaises(CommandError):
            UtilsCommand.call("is_str_in_file", "", self.fp.name)


class TestIsLineInFile(TestCase):

    def setUp(self):
        self.fp = module.tempfile.NamedTemporaryFile()
        self.fp.write(b'This is a test\ntest success\nwow')
        self.fp.flush()

    def tearDown(self):
        self.fp.close()

    def test1(self):
        result = UtilsCommand.call(
            "is_line_in_file", "test success", self.fp.name,
        )
        self.assertEqual(result.code, 0)

        with self.assertRaises(CommandError):
            try:
                UtilsCommand.call("is_line_in_file", "test fail", self.fp.name)
            except CommandError as error:
                self.assertNotEqual(error.result.code, 0)
                self.assertEqual(error.result.stderr, "")
                raise

    def test2(self):
        with self.assertRaises(CommandError):
            UtilsCommand.call("is_line_in_file", "", self.fp.name)


class TestWriteLineOnce(TestCase):

    def setUp(self):
        self.fp = module.tempfile.NamedTemporaryFile()

    def tearDown(self):
        self.fp.close()

    def read(self):
        self.fp.seek(0)
        return self.fp.read()

    def test1(self):
        self.assertEqual(self.read(), "")
        result = UtilsCommand.check_call(
            "append_line_once", "test success", self.fp.name,
        )
        self.assertEqual(result, "ok\n")
        self.assertEqual(self.read(), "test success\n")
        result = UtilsCommand.check_call(
            "append_line_once", "test success", self.fp.name,
        )
        self.assertEqual(result, "skip\n")
        self.assertEqual(self.read(), "test success\n")

# end file
