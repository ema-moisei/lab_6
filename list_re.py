"""3. Write a function that receives two parameters: a list of strings and a list of regular expressions.
The function will return a list of the strings that match on at least one regular expression from the list given
as parameter."""

import re


def function(re_list, text_list):
    my_list = []
    for reg in re_list:
        for text in text_list:
            if re.findall(reg, text):
                my_list.append(text)

    return my_list


def main():
    re1 = "[a-d]"
    re2 = "[G-L]$"
    re3 = "^beg"
    re_list = [re1, re2, re3]
    text_list = ["characters are at the beginning of the string", "ExactlG thH specified",  "838 efg"]
    my_list = function(re_list, text_list)
    print(my_list)


if __name__ == "__main__":
    main()
