"""8. Write a function that recursively scrolls a directory and displays those files whose name matches a regular
expression given as a parameter or contains a string that matches the same expression.
Files that satisfy both conditions will be prefixed with ">>" """

import re
import os


def re_scrolls(path, regex):
    matches = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            print(file, "ss")
            if re.match(regex, file):
                matches.append(file)
            new_path = os.path.join(dirpath, file)
            if os.path.isfile(new_path):
                handler = open(new_path, "r")
                line = handler.readline().strip()
                while line:
                    if re.match(regex, file):
                        if filenames in matches:
                            matches[file] = ">>" + file
                        else:
                            matches.append(file)
                    line = handler.readline()
                handler.close()
    return matches


def main():
    path = "D:\\test\\1"
    regex = "\w+"
    matches = re_scrolls(path, regex)
    print(matches)


if __name__ == "__main__":
    main()

