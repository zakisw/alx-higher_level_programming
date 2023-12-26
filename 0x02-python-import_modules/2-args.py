#!/usr/bin/python3
import sys


def print_arguments():
    # Total number of arguments
    # Subtract 1 to exclude the script name itself
    total_args = len(sys.argv) - 1

    # List of arguments
    args_list = sys.argv[1:]  # Exclude the script name
    if total_args <= 0:
        print("{} arguments.".format(total_args))
    elif total_args == 1:
        print("{} argument:".format(total_args))
        print(f"{total_args}: {' '.join(args_list)}")
    else:
        print("{} arguments:".format(total_args))
        print(f"{total_args}: {' '.join(args_list)}")


if __name__ == "__main__":
    print_arguments()
