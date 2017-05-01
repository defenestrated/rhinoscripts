import rhinoscriptsyntax as rs
import random
import math


obj = rs.GetObject("Select a curve", rs.filter.curve)
numCoils = rs.GetInteger("number of coils")

if obj:
    point = rs.CurveStartPoint(object)
    if point:
        param = rs.CurveClosestPoint(obj, point)
        normal = rs.CurveTangent(obj, param)
        print normal

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
    #         rs.AddPoint([x,y,z])
            points.append([x,y,z])
            i += inc
    rs.AddInterpCurve(points)