import sys

import spellcheck, gingerspell

text = str(sys.argv[1])
# gingerspell

result = gingerspell.correct("hellp")
print(result)

# spell_check

# result2 = spellcheck.correct("narth")
# print(result2)
