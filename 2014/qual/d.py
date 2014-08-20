#!/usr/bin/env python3

"""
Google Code Jam
Qualification Round 2014
Problem D. Deceitful War
"""

import argparse
import copy
import random

class TestCase:
    def __init__(self, blocks_naomi, blocks_ken):
        self.blocks_naomi = blocks_naomi
        self.blocks_ken = blocks_ken
    def war(self):
        score_naomi = 0
        blocks_naomi = copy.copy(self.blocks_naomi)
        blocks_ken = copy.copy(self.blocks_ken)
        while len(blocks_naomi) > 0:
            chosen_naomi = random.sample(blocks_naomi, 1)[0]
            good_blocks = set([x for x in blocks_ken if x > chosen_naomi])
            if len(good_blocks) > 0:
                chosen_ken = min(good_blocks)
            else:
                chosen_ken = min(blocks_ken)
                score_naomi += 1
            blocks_naomi.remove(chosen_naomi)
            blocks_ken.remove(chosen_ken)
        return score_naomi
    def dwar(self):
        score_naomi = 0
        blocks_naomi = copy.copy(self.blocks_naomi)
        blocks_ken = copy.copy(self.blocks_ken)
        while len(blocks_naomi) > 0:
            # Naomi can (and should) always force
            # Ken to choose his heaviest block
            chosen_ken = max(blocks_ken)
            if max(blocks_naomi) < chosen_ken:
                chosen_naomi = min(blocks_naomi)
            else:
                chosen_naomi = max(blocks_naomi)
                score_naomi += 1
            blocks_naomi.remove(chosen_naomi)
            blocks_ken.remove(chosen_ken)
        return score_naomi

def read_input(filename):
    with open(filename) as f:
        num_test_cases = int(next(f))
        test_cases = []
        for _ in range(num_test_cases):
            num_blocks = int(next(f))
            blocks_naomi = [float(x) for x in next(f).split()]
            blocks_ken = [float(x) for x in next(f).split()]
            test_case = TestCase(blocks_naomi, blocks_ken)
            test_cases.append(test_case)
    return test_cases

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="input file")
    args = parser.parse_args()
    test_cases = read_input(args.filename)
    num_test_case = 1
    for test_case in test_cases:
        print("Case #{}:".format(num_test_case), test_case.dwar(), test_case.war())
        num_test_case += 1