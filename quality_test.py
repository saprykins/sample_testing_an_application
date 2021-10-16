# pip install pytest in bash
# to launch the test
# type the command $ pytest quality_test.py
# quality_test.py and python_script.py are in the same folder

import python_script
import unittest

from python_script import main_Func_from_python_script


class TestStringMethods(unittest.TestCase):
    def tests(self):
        self.assertEqual(main_Func_from_python_script(), 'hello')
        
