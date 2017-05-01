# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import math
import time

numCoils = rs.GetInteger("number of coils")

if numCoils:
    points = []
    coilCount = 0
    x = 0
    y = 0
    z = 0
    i = 0
    direction = [0,0,0]
    theta = 0
    phi = 0
    end = numCoils*(2*math.pi)
    inc = math.pi/4
    
    while coilCount < numCoils:
        while i < end:
            x = math.cos(i)
            y = math.sin(i)
            z += inc
            theta += inc
            if theta >= 2*math.pi:
                coilCount += 1
                theta = 0
            rs.AddPoint([x,y,z])
#             points.append([x,y,z])
            i += inc
            rs.Redraw()
            time.sleep(1)
#     rs.AddInterpCurve(points)
        
else:
    print "numCoils is empty"