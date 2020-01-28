#!/usr/bin/env python3

import random
import argparse

parser = argparse.ArgumentParser(description='Roll the dice.')
parser.add_argument('rolls', type=int, help='an integer number of times to roll')
args = parser.parse_args()

results = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
}

def rollOnce():
  global results
  val = random.randrange(1,7)
  if val in results:
    results[val] = results[val]+1

def rollMany(num_rolls):
  for i in range(num_rolls):
    rollOnce()

roll_count = vars(args)['rolls']
print(f'Rolling the dice {roll_count} times:')
rollMany(roll_count)
print(results)

for (val, cnt) in results.items():
  pct = round(cnt / roll_count * 100, 1)
  print(f'Roll {val}: {cnt} ({pct}%)')
