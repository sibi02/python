import re

# pattern = '^a...s$'
# test_string = 'abass'
# result = re.match(pattern,test_string)

# print(result)

test_string_1='Geeks for Geeks: A computer science portal for geeks'

# match = re.match(r'portal',test_string_1)
match = re.search(r'for',test_string_1)

# print(match)
print(match.group())

# print(match.start())
# print(match.end())

# print(match.span())

# print(match.group())

find_string = re.findall(r'for',test_string_1)
print(find_string)

print('Range',re.search(r'[a-zA-Z]','x'))