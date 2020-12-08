from rtreelib import RTree, Rect
from rtreelib.diagram import create_rtree_diagram
import csv
import os
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz 2.44.1\bin'


# Create an RTree instance with some sample data
t = RTree(max_entries=4)
t.insert('a', Rect(0, 0, 3, 3))
t.insert('b', Rect(2, 2, 4, 4))
t.insert('c', Rect(1, 1, 2, 4))
t.insert('d', Rect(8, 8, 10, 10))
t.insert('e', Rect(7, 7, 9, 9))

# Create a diagram of the R-tree structure
#create_rtree_diagram(t)


f=open('normal_.csv', 'r', encoding='utf-8')
reader=csv.reader(f)
for i in reader:
    id, category, x, y = i

    if id == "id":
        continue
    print(x+" "+y)

    #
    # processing
    #

f.close()