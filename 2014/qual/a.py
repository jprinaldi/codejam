#!/usr/bin/env python3

"""
Google Code Jam
Qualification Round 2014
Problem A. Minesweeper Master
"""

class TestCase:
    def __init__(self, first_answer, second_answer, first_grid, second_grid):
        self.first_answer = first_answer
        self.second_answer = second_answer
        self.first_grid = first_grid
        self.second_grid = second_grid
    def __repr__(self):
        return "{} {}".format(self.first_answer, self.second_answer)
    def solve(self):
        first_possible_cards = set(self.first_grid[self.first_answer - 1])
        second_possible_cards = set(self.second_grid[self.second_answer - 1])
        possible_cards = first_possible_cards.intersection(second_possible_cards)
        num_possible_cards = len(possible_cards)
        if num_possible_cards == 0: return "Volunteer cheated!"
        elif num_possible_cards == 1: return next(iter(possible_cards))
        else: return "Bad magician!"

def read_data(filename):
    with open(filename) as f:
        test_cases = []
        num_test_cases = int(f.readline())
        for _ in range(num_test_cases):
            first_answer = int(f.readline())
            first_grid = []
            for _ in range(4):
                row = [int(x) for x in f.readline().split()]
                first_grid.append(row)
            second_answer = int(f.readline())
            second_grid = []
            for _ in range(4):
                row = [int(x) for x in f.readline().split()]
                second_grid.append(row)
            test_case = TestCase(first_answer, second_answer, first_grid, second_grid)
            test_cases.append(test_case)
    return num_test_cases, test_cases

if __name__ == "__main__":
    num_test_cases, test_cases = read_data("A-small-practice.in")
    for it in range(num_test_cases):
        test_case = test_cases[it]
        print("Case #{}:".format(it + 1), test_case.solve())