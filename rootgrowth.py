# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import math
import Rhino

numRoots = rs.GetInteger("Number of roots")
mincount = rs.GetInteger("min points per root")
maxcount = rs.GetInteger("max points per root")

startpoint = rs.GetPoint("seed point")
print "seed point: ", startpoint[0], " / ", startpoint[1], " / ", startpoint[2]

pi = math.pi

if mincount and maxcount and numRoots:

    for a in range(numRoots):
        count = random.randint(mincount, maxcount)
        points = []
        x = startpoint[0]
        y = startpoint[1]
        z = startpoint[2]
        points.append([startpoint[0], startpoint[1], startpoint[2]])
        offset = 0
        dangle = random.random()*10
        for i in range(count):
            offset = math.sin(pi*(i/count)*0.6)*dangle
            x = random.random()*0.5 + offset + startpoint[0]
            y = random.random()*0.5 + startpoint[1]
            z -= (maxcount-mincount)/10 + startpoint[2]
            # rs.AddPoint([x,y,z])
            points.append([x,y,z])
        thiscurve = rs.AddInterpCurve(points)
        rs.RotateObject(thiscurve, startpoint, random.random()*360)

    rs.ZoomExtents(view=None, all=True)
