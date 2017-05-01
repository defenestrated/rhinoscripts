# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import sys
import Rhino

def connect(objects):
    points = []

    c = rs.GetPoint("inclusion radius - center")
    if not c: sys.exit("no center point specified")
    r = rs.GetPoint("inclusion radius - distance")
    if not c: sys.exit("no distance specified")

    maxradius = rs.Distance(c, r)

    blen = len(objects)
    print "before: ", blen, " objects"

    for i in range(len(objects)-1):
        if rs.IsPoint(objects[i]):
            points.append(objects[i])

    alen = len(points)

    print "after: ", alen, " objects"

    for j in range(len(points)-1):
    # for each point,
        for k in range(len(points)-1):
            # go through each of the other objects:
            p1 = points[j]
            p2 = points[k]
            if p1 != p2:
                if rs.Distance(p1, p2) < maxradius:
                    rs.AddLine(p1, p2)

objlist = rs.SelectedObjects()
if objlist:
    connect(objlist)
else:
    pts = rs.GetObjects("select points", filter=1)
    connect(pts)
