# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import Rhino
# from scipy import constants as


count = rs.GetInteger("Number of lines")
exp = rs.GetReal("multiplication ratio")
rotations = rs.GetReal("number of rotations")
# print]
points = []

length = 1
counter = 1
theta = 0
origin = [0,0,0]
# rs.AddLine(origin, [0,length,0])

if count:
    for i in range(count):
        length *= exp
        theta += 10
        thisline = rs.AddLine(origin, [0,length,0])
        point = rs.AddPoint([0,length,0])
        rs.RotateObject(thisline, origin, (360*rotations/count)*i)
        rs.RotateObject(point, origin, (360*rotations/count)*i)
        points.append(point)


    rs.AddInterpCurve(points)
    rs.DeleteObjects(rs.ObjectsByType(1))
