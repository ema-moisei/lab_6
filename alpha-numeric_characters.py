"""1. Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
alpha-numeric characters."""

import re


def alpha_numeric_characters(text):
    regex = "[a-zA-Z0-9]{2,50}"
    my_list = re.findall(regex, text)

    return my_list


def main():
    text = "found substring 00123 starti,,,,ng at index 3 and ending ;'/. g at index 8"
    my_list = alpha_numeric_characters(text)
    print(my_list)


if __name__ == "__main__":
    main()
