#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is a program that shows numbers from 1000-2000

import math


def main():
    # This is a program that shows numbers from 1000-2000

    counter = 1000

    for counter in range(1000, 2001):

        print(counter, end=" ")

        if counter % 5 == 0:
            print("")


if __name__ == "__main__":
    main()
