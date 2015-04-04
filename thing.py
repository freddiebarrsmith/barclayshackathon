from collections import OrderedDict

with open('forgmaps.csv') as fin:
    lines = (line.rstrip() for line in fin)
    unique_lines = OrderedDict.fromkeys( (line for line in lines if line) )

print unique_lines.keys()