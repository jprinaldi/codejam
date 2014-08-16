#!/usr/bin/env python3

"""
Google Code Jam
Qualification Round 2014
Problem B. Cookie Clicker Alpha
"""

import argparse

class TestCase:
    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X
        self.cookies = 0
        self.cookie_rate = 2
        self.elapsed_time = 0
    def can_buy(self):
        return self.cookies >= self.C
    def should_buy(self):
        remaining_cookies = self.X - self.cookies
        remaining_time = remaining_cookies/self.cookie_rate
        if self.can_buy():
            return remaining_time >= (remaining_cookies + self.C)/(self.cookie_rate + self.F)
        else:
            return remaining_time >= (self.C - self.cookies)/self.cookie_rate + self.X/(self.cookie_rate + self.F)
    def buy(self):
        self.cookies -= self.C
        self.cookie_rate += self.F
    def solve(self):
        while True:
            if not self.should_buy():
                self.elapsed_time += (self.X - self.cookies)/self.cookie_rate
                return self.elapsed_time
            if not self.can_buy():
                self.elapsed_time += (self.C - self.cookies)/self.cookie_rate
                self.cookies = self.C
            self.buy()

def read_input(filename):
    with open(filename) as f:
        num_test_cases = int(next(f))
        test_cases = []
        for _ in range(num_test_cases):
            C, F, X = [float(n) for n in next(f).split()]
            test_case = TestCase(C, F, X)
            test_cases.append(test_case)
    return num_test_cases, test_cases

def solve_input(filename):
    num_test_cases, test_cases = read_input(filename)
    for it in range(num_test_cases):
        print("Case #{}:".format(it + 1), round(test_cases[it].solve(), 7))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="input file")
    args = parser.parse_args()
    solve_input(args.filename)
