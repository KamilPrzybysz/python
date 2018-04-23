import re from string import whitespace from collections import Counter 
SENTENCES = re.compile(r'([A-Z].*?\.)(?=(\s[A-Z]|\Z))', re.DOTALL) def 
stats(string):
    chars_stats = Counter(string).most_common()
    chars_stats = '\n'.join(
        '{} {}'.format(char, count)
        for char, count in chars_stats
        if char not in whitespace
    )
    print('\n{}'.format(chars_stats))
    print("\n\n\n"+str(chars_stats)) i=int(input()) if i>150:
  exit() else:
  a=""
  for x in range(i):
    a=a+str(input())
  stats(a)
