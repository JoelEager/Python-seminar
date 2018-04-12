"""
So in Python functions are objects. Using that and docstrings you can do fun stuff like this.
    Run "python cmdDemo.py" for usage info.
"""

import sys

def add():
    """
    Usage: python3 cmdDemo.py add <number 1> <number 2>
    """
    result = float(sys.argv[2]) + float(sys.argv[3])
    print(sys.argv[2] + " + " + sys.argv[3] + " = " + str(result))

def even():
    """
    Usage: python3 cmdDemo.py even <number>
    """
    result = (float(sys.argv[2]) % 2) == 0
    print("isEven(" + sys.argv[2] + ") = " + str(result))

commands = {
    "add": add,
    "even": even
}

def main():
    if len(sys.argv) >= 2:
        command = str(sys.argv[1]).lower()

        if command in commands:
            try:
                commands[command]()
            except (ValueError, IndexError):
                print(commands[command].__doc__.strip())

            return

    print("Valid commands:")
    for name, funct in commands.items():
        print("\t" + name + " - " + funct.__doc__.strip())

    print("\nCommands are case insensitive.")

if __name__ == "__main__":
    main()