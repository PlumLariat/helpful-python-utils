import typing
import sys
import re


def longest_line(file: typing.TextIO) -> int:
    longest = 0
    contents = file.readlines()

    for line in contents:
        if len(line) > longest:
            longest = len(line)
    
    return longest

def main():
    args = sys.argv

    pattern = "\S+.txt"

    if len(args) == 1:
        print("You have to give me a file to count dummy.")
    else:

        if len(args) > 2:
            print("This program will only take one file argument.")
            for i in range(2,len(args)):
                print(f"{args[i]} will not be read.")
                print("continuing execution.")

        try:
            match = re.match(pattern, args[1])
            print(match.group())

            f = open(match.group(), "r")
            print(longest_line(f))

        except AttributeError as a:
            print(f"The file: {args[1]}, is not a text file.")
            print("terminating execution...")
        except FileNotFoundError as fe:
            print(fe)

if __name__ == "__main__":
    main()