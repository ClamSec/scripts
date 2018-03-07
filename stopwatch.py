#! /usr/bin/python3
"""Keep track of elapsed time."""


import time
import datetime


def main():
    """Track the progression of time."""
    time_elapsed = 0.0
    while (True):
        time_string = datetime.timedelta(seconds=time_elapsed)
        print('\t', time_string, end='\r')
        time.sleep(1.0)
        time_elapsed += 1.0


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKeyboard interrupt. Exiting.")
        exit()
