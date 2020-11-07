# -------------------------------------------------------------------------------
# (c) 2020 Thomas Graf
# All Rights Reserved.
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

import sys
import unittest

sys.path.insert(1, "..")

import mylibrary


class MyLibraryTest(unittest.TestCase):
    def test_check_operands(self):
        lib = mylibrary.MyLibrary()
        actual = lib.check_operands(1, 5)
        self.assertTrue(actual)

        actual = lib.check_operands("x", 5)
        self.assertFalse(actual)

        actual = lib.check_operands(1, 5.5)
        self.assertFalse(actual)

        actual = lib.check_operands(1.5, "5")
        self.assertFalse(actual)

    def test_operation_add(self):
        lib = mylibrary.MyLibrary()
        actual = lib.operation_add(1, 5)
        self.assertEqual(6, actual)

    def test_operation_add_invalid_operands(self):
        lib = mylibrary.MyLibrary()
        with self.assertRaises(mylibrary.LibraryError):
            lib.operation_add(1, "x")

    def test_operation_subtract(self):
        lib = mylibrary.MyLibrary()
        actual = lib.operation_subtract(5, 2)
        self.assertEqual(3, actual)

    def test_operation_subtract_invalid_operands(self):
        lib = mylibrary.MyLibrary()
        with self.assertRaises(mylibrary.LibraryError):
            lib.operation_subtract("5", 2)

    def test_operation_multiply(self):
        lib = mylibrary.MyLibrary()
        actual = lib.operation_multiply(2, 5)
        self.assertEqual(10, actual)

    def test_operation_multiply_invalid_operands(self):
        lib = mylibrary.MyLibrary()
        with self.assertRaises(mylibrary.LibraryError):
            lib.operation_multiply("", 5)

    def test_operation_divide(self):
        lib = mylibrary.MyLibrary()
        actual = lib.operation_divide(6, 2)
        self.assertEqual(3, actual)

    def test_operation_divide_invalid_operands(self):
        lib = mylibrary.MyLibrary()
        with self.assertRaises(mylibrary.LibraryError):
            lib.operation_divide(6, 2.2)

    def test_operation_divide_by_zero(self):
        lib = mylibrary.MyLibrary()
        with self.assertRaises(mylibrary.LibraryError):
            lib.operation_divide(6, 0)


if __name__ == "__main__":
    unittest.main()