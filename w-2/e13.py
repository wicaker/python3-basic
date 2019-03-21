# https://github.com/hacktiv8/phase-0-activities/blob/master/modules/challenge-x-dan-o.md
# regex

import re

def xo(str):
  x = re.findall("x", str)
  o = re.findall("o", str)
  if(len(x) == len(o)):
    return True
  return False

# TEST CASES
print(xo('xoxoxo')) # true
print(xo('oxooxo')) # false
print(xo('oxo')) # false
print(xo('xxxooo')) # true
print(xo('xoxooxxo')) # true