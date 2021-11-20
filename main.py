"""
Dictionary Challenge 2 - Destination City

Description:
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example:
Input:
  paths = [
    ["London","New York"],
    ["New York","Lima"],
    ["Lima","Sao Paulo"]
  ]
  start = "London"
Correct Output:
  "Sao Paulo"
"""

from solutions import fast


########
# Write your code in this function
########
def solution(paths, start):
  return fast(paths, start)


########
# This code wil run your solution against a bunch of test cases
########
from tests.runner import run

if __name__ == "__main__":
  run(solution)