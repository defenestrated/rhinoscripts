# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import math
import Rhino

numCyls = rs.GetInteger("Number of sticks")
spread = rs.GetInteger("spread")

seed = rs.GetPoint("seed point")
print "seed point: ", seed[0], " / ", seed[1], " / ", seed[2]

pi = math.pi

if numCyls and spread and seed:

    for a in range(numCyls):
        x = seed[0]
        y = seed[1]
        z = seed[2]
        # points.append([seed[0], seed[1], seed[2]])
        offset = random.random()*spread
        stick = rs.AddCylinder([x + offset, y, z], random.random()*10, random.random()*0.5, True)
        rs.RotateObject(stick, seed, random.random()*360)

    rs.ZoomExtents(view=None, all=True)
