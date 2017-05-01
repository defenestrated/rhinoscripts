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
    
    xadd = 0
    yadd = 0
    
    rmin = 1
    rmax = 20
    toggle = 1
    
    rs.AddPoint([x,y,z])
    points.append([x,y,z])
    
    for i in range(count):
#         time.sleep(0.001)
        
        xadd = random.randint(rmin, rmax)
        yadd = random.randint(rmin, rmax)
        
        if (i%2 == 0):
            toggle *= -1
            xadd *= toggle
            x += xadd
            
            
        else:
            yadd *= toggle
            y += yadd
            
#         rmin += 1
#         rmax += 1
        
        
        rs.AddPoint([x,y,z])
        points.append([x,y,z])
#        print(i)
#         Rhino.RhinoApp.Wait()
#     rs.HideObjects(rs.ObjectsByType(1))
    rs.DeleteObjects(rs.ObjectsByType(1))
    rs.AddInterpCurve(points)
#     rs.AddPolyline(points)
        
