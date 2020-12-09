from rtreelib import RTree, Rect
from rtreelib.diagram import create_rtree_diagram
import csv

t = RTree()
M = 0.0000001

f = open('normal.csv', 'r', encoding='utf-8')
val = csv.reader(f)
for i in val:
    identity, category, x, y = i

    if identity == "id":
        continue
    if int(identity) > 10:
        break
    x = float(x)
    y = float(y)
    t.insert(identity, Rect(x, y, x + M, y + M))

create_rtree_diagram(t)

f.close()
