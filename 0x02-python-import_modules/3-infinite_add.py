#!/usr/bin/python3
import sys


def print_arguments():
    # Total number of arguments
    # Subtract 1 to exclude the script name itself
    total_args = len(sys.argv) - 1

    # List of arguments
    args_list = sys.argv[1:]  # Exclude the script name
    if total_args == 0:
        print("{}".format(total_args))
    else:
        add = 0
        for i in range(1, total_args + 1):
            sys.argv[i] = int(sys.argv[i])
            add += sys.argv[i]

        print(f"{add}")


if __name__ == "__main__":
    print_arguments()
