# coding: utf-8
import os
from collections import namedtuple
from subprocess import Popen, PIPE


class Module(object):
    def __getattr__(self, name):
        module = __import__(name)
        setattr(self, name, module)
        return module
        
module = Module()


class Command(object):
    class CommandError(Exception):
        def __init__(self, result, *args, **kwargs):
            self.result = result
            super(CommandError, self).__init__(*args, **kwargs)

    CommandResult = namedtuple("CommandResult", ["code", "stdout", "stderr"])
    
    def __init__(self, utils_path):
        self.utils_path = utils_path
        
    def call_command(self, command, args=(), stdin=None):
        shell = [self.utils_path, command]
        shell.extend(args)
        process = Popen(
            shell, shell=False,
            stdin=PIPE, stdout=PIPE, stderr=PIPE,
        )
        stdout, stderr = process.communicate(stdin)
        code = process.poll()
        result = self.CommandResult(code=code, stdout=stdout, stderr=stderr)
        if code != 0:
            raise self.CommandError(result, stderr)
        return result


class UtilsCommand(Command):
    def __init__(self, postfix=None):
        if postfix is True:
            postfix = os.getenv("IMAGE_TYPE", "")
        root = os.path.dirname(os.path.dirname(__file__))
        utils_name = "utils/utils{postfix}.sh".format(
            postfix="_%s" % postfix if postfix else ""
        )
        utils_path = os.path.join(root, utils_name)
        super(UtilsCommand, self).__init__(utils_path)
        
    @classmethod
    def call(cls, command, *args):
        cmd = cls()
        return cmd.call_command(command, args)
        
    @classmethod
    def postfix_call(cls, command, *args):
        cmd = cls(True)
        return cmd.call_command(command, args)