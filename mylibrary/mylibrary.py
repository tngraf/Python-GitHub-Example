# -------------------------------------------------------------------------------
# (c) 2020 Thomas Graf
# All Rights Reserved.
#
# Licensed under the MIT license.
# SPDX-License-Identifier: MIT
# -------------------------------------------------------------------------------

"""This is a demo/test Python project"""


class LibraryError(Exception):
    """Base exception for operations

    :param message: a general error message
    :type message: string
    """

    def __init__(self, message=None):
        self.message = message


class MyLibrary:
    """Python test interface"""

    def check_operands(self, a: int, b: int):
        """
        Check the operands for being integer values.

        :param a: first operand
        :type a: int
        :param b: second operand
        :type b: int
        :return: True if both operands are integers
        :rtype: bool
        """
        if not isinstance(a, int):
            return False

        if not isinstance(b, int):
            return False

        return True

    def operation_add(self, a: int, b: int):
        """
        Add two integer values.

        :param a: first operand
        :type a: int
        :param b: second operand
        :type b: int
        :return: the addition result
        :rtype: int
        """
        if not self.check_operands(a, b):
            raise LibraryError("Invalid operands")

        return a + b

    def operation_subtract(self, a: int, b: int):
        """
        Subtract two integer values.

        :param a: first operand
        :type a: int
        :param b: second operand
        :type b: int
        :return: the subtraction result
        :rtype: int
        """
        if not self.check_operands(a, b):
            raise LibraryError("Invalid operands")

        return a - b

    def operation_multiply(self, a: int, b: int):
        """
        Multiply two integer values.

        :param a: first operand
        :type a: int
        :param b: second operand
        :type b: int
        :return: the multiplication result
        :rtype: int
        """
        if not self.check_operands(a, b):
            raise LibraryError("Invalid operands")

        return a * b

    def operation_divide(self, a: int, b: int):
        """
        Divide two integer values.

        :param a: first operand
        :type a: int
        :param b: second operand
        :type b: int
        :return: the division result
        :rtype: int
        """
        if not self.check_operands(a, b):
            raise LibraryError("Invalid operands")

        if b == 0:
            raise LibraryError("You must not divide by zero")

        return a / b
