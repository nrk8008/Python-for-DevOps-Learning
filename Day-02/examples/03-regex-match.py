import re

text = "The quick brown fox"
pattern = r"quick"

match1 = re.match(pattern, text)
match2 = re.search(pattern, text)
if match1:
    print("Match found:", match1.group())
else:
    print("No match")

if match2:
    print("Match found", match2.group())
else: 
    print("No match")

