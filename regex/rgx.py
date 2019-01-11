import re

my_str = 'an example word:cat!!'
print(my_str)
match = re.search(r'a\w*e', my_str)
# If-statement after search() tests if it succeeded
if match:
  print ('found', match.group()) ## 'found word:cat'
else:
  print ('did not find')

match = re.search(r'\d\s*\d\s*\d', 'xx134242  3xx')
print(match.group())


