# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import Rhino


count = rs.GetInteger("Number of points")
points = []
if count:
    x = 0
    y = 0
    z = 0
#     points.append([x,y,z])
    for i in range(count):
    	time.sleep(0.1)
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z += 0.5
        rs.AddPoint([x,y,z])
        points.append([x,y,z])
        Rhino.RhinoApp.Wait()
    rs.AddInterpCurve(points)
