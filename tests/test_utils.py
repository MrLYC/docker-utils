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
