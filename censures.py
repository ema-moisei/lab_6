"""6.Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
Censorship means replacing characters from odd positions with *."""

import re


def censure(text):
    censured = ""
    regex = "^[aeiouAEIOU]|\\w+[aeiouAEIOU]\\b"
    text = text.split()
    for word in text:
        if re.match(regex, word):
            poz = 1
            new_word = ""
            for letter in word:
                if poz % 2 != 0:
                    new_word += "*"
                else:
                    new_word += letter
                poz += 1
            censured += new_word + " "
        else:
            censured += word + " "

    return censured


def main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua."
    censured = censure(text)
    print(censured)


if __name__ == "__main__":
    main()
