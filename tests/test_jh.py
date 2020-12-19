from rtreelib import RTree, Rect
from rtreelib.diagram import create_rtree_diagram
import csv
from rtreelib.pg import init_db_pool, create_rtree_tables, export_to_postgis, clear_rtree_tables

t = RTree()
M = 0.0000001

f = open('normal.csv', 'r', encoding='utf-8')
val = csv.reader(f)
for i in val:
    identity, category, x, y = i

    if identity == "id":
        continue
    if int(identity) > 10000:
        break
    x = float(x)
    y = float(y)
    t.insert(identity, Rect(x, y, x + M, y + M))

#create_rtree_diagram(t)    # too busy

f.close()

init_db_pool(user="postgres", password="dlwjdgns1587", database="rtreelib_10000")

create_rtree_tables(srid=4326)

rtree_id = export_to_postgis(t, srid=4326)


# cleaning table
clear_rtree_tables()