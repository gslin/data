#!/usr/bin/env python3

import itertools
import sys

class Main():
    def main(self):
        costs = list(map(lambda x: int(x), sys.argv[1:]))

        for cnt in range(1, len(costs) + 1):
            for item in itertools.combinations(costs, cnt):
                cost = sum(item)
                print('{}: {}'.format(cost, list(item)))

if __name__ == '__main__':
    Main().main()
