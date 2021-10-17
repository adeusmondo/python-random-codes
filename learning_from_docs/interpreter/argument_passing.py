# 2.1.1 Argument Passing

import sys

def main():
    """
        When you pass additional arguments, you
        can access them this way.

        When no script and no arguments are given,
        sys.argv is a empty list.

        When you pass a script, the firt position in
        sys.argv is the name of the script.

        When your pass another command '-c', '-m' or
        something else, this is place in sys.argv[0].

        Example: python python interpreter/argument_passing.py 'primeiro item' 'segundo item'

        Output:
            argv[0] :: interpreter/argument_passing.py
            argv[1] :: primeiro item
            argv[2] :: segundo item
    """
    for i, arg in enumerate(sys.argv):
        print(f"argv[{i}] :: {arg}")


if __name__ == "__main__":
    main()