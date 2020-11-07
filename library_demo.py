# -------------------------------------------------------------------------------
# (c) 2020 Thomas Graf
# All Rights Reserved.
#
# Licensed under the MIT license.
# -------------------------------------------------------------------------------

"""
Simple demo application that uses MyLibrary
"""

import argparse
import sys
from colorama import init, Fore, Style

import mylibrary

# intialize colorama
init()


class MyLibraryDemo:
    """Demonstrate MyLibrary"""

    def check_operation(self, operation: str):
        operation = operation.lower()
        return operation in ["add", "subtract", "multiply", "divide"]

    @classmethod
    def parse_commandline(cls):
        """Parse command line arguments"""
        parser = argparse.ArgumentParser(
            description="Test MyLibrary"
        )

        parser.add_argument(
            "arguments",
            nargs = "+",
            help="operation to perform",
        )

        parser.add_argument(
            "-v",
            "--verbose",
            help="be verbose",
            action="store_true",
        )

        args = parser.parse_args()

        return args

    def main(self):
        """Main method()"""
        print("\nTest MyLibrary")

        args = self.parse_commandline()
        if len(args.arguments) < 3:
            sys.exit(
                Fore.LIGHTRED_EX +
                "Error: Not enough arguments specified!" +
                Style.RESET_ALL)

        if not self.check_operation(args.arguments[0]):
            sys.exit(
                Fore.LIGHTRED_EX +
                "Error: No valid operation specified: " +
                args.arguments[0] +
                Style.RESET_ALL)

        lib = mylibrary.MyLibrary()

        try:
            result = None
            operation = args.arguments[0].lower()
            a = int(args.arguments[1])
            b = int(args.arguments[2])

            if operation == "add":
                result = lib.operation_add(a, b)
            elif operation == "subtract":
                result = lib.operation_subtract(a, b)
            elif operation == "multiply":
                result = lib.operation_multiply(a, b)
            elif operation == "divide":
                result = lib.operation_divide(a, b)

            print("Result = " + str(result))
        except Exception as ex:
            sys.exit(
                Fore.LIGHTRED_EX +
                "Error: " + repr(ex) +
                Style.RESET_ALL)


if __name__ == "__main__":
    APP = MyLibraryDemo()
    APP.main()
