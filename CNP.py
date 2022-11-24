"""7. Verify using a regular expression whether a string is a valid CNP."""

import re


def check_valid_CNP(string):
    regex = "([1-8])([0-9][0-9])((0[1-9])|(1[12]))(([0-2][1-9])|(3[01]))(([0-3][1-9])|(4[0-8])|(5[12]))" \
            "(([0-9][0-9][1-9])|([1-9][0-9]{2})|([0-9][1-9][0-9]))([0-9])"
    if re.match(regex, string):
        return True
    return False


def main():
    v_cnp = "1950205220028"
    i_cnp = "05588562456213"
    validation = check_valid_CNP(i_cnp)
    if validation:
        print("The string is a valid CNP")
    else:
        print("The string does not represent a valid CNP")


if __name__ == "__main__":
    main()
