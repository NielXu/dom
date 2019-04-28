import re


def flat(d):
    """
    Read lines of file and strip whitespaces on both sides.
    The multi-lines file will be merged to one line and
    separated by a whitespace.
    """
    f = open(d, "r")
    lines = f.readlines()
    s = ""
    for i in lines:
        s += i.strip() + " "
    return s[:-1]


if __name__ == "__main__":
    print(flat("test/test.html"))