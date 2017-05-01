# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import Rhino

points = rs.SelectedObjects()
exaggerate = rs.GetReal("exaggeration multiplier (try it first and then adjust, default is 1.0)")
repeat = rs.GetInteger("number of times to repeat (skip for single execution)")

if not repeat:
    repeat = 1

if not exaggerate:
    exaggerate = 1.0
    print("no dice")
    print(exaggerate)
else:
    print("multiplier supplied")
    print(exaggerate)

print("exaggeration: ", exaggerate, " :: repeating ", repeat, " times")

for time in range(repeat):
    for pt in points:
        translation = [(random.random()-0.5)*exaggerate, (random.random()-0.5)*exaggerate, (random.random()-0.5)*exaggerate]
        rs.MoveObject(pt, translation)
    rs.AddInterpCurve(points)
