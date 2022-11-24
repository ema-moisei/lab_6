"""2. Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns
those long-length x substrings that match the regular expression."""

import re


def substrings(regex, text, x):
    my_list = []
    my_regex = regex + "{" + str(x) + "}"
    print(my_regex)

    my_list = re.findall(my_regex, text)

    return my_list


def main():
    regex = "[a-z]"
    text = "found fgh substring 00123 ert starti,,,,ng at index 3 and ending ;'/. g at index 8"
    x = 3
    my_list = substrings(regex, text, x)
    print(my_list)


if __name__ == "__main__":
    main()
