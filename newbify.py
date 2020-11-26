import re
from random import randint


with open("newbify.py") as f:
    lines = [line for line in f.readlines()]

fuxd_lines = []
for line in lines:
    #for symbol in ['[', ']', '(', ')', ':', ',', '==', '=']:
    for symbol in ['[', ']', '(', ')', ':', ',', '==', '=']:
        # Do not alter shit in strings
        if not re.search(f'''(\".*\{symbol}.*\")|(\'.*\{symbol}.*\')''', line):
            line = line.replace(symbol, f'{randint(5, 25)*" "}{symbol}{randint(5, 25)*" "}' )
            # if symbol == "==":
            #     line = line.replace("==", '$$')
            # if symbol == "=":
            #     line = line.replace('$$', '==')

    if re.search(r"^[\t ]*if", line):
        line = line.replace("if", f'if{randint(5, 25)*" "}' )
    if re.search(r"^[\t ]*for", line):
        line = line.replace("for", f'for{randint(5, 25)*" "}' )
    if re.search(r"^[\t ]*while", line):
        line = line.replace("while", f'while{randint(5, 25)*" "}' )
    if re.search(r"^[\t ]*with", line):
        line = line.replace("with", f'with{randint(5, 25)*" "}' )
    if re.search(r"^[\t ]*def", line):
        line = line.replace("def", f'def{randint(5, 25)*" "}' )
    if re.search(r"^[\t ]*class", line):
        line = line.replace("class", f'class{randint(5, 25)*" "}' )
    fuxd_lines.append(line)

with open("fucked_lines", "w") as f:
    f.writelines(fuxd_lines)
print(fuxd_lines)
