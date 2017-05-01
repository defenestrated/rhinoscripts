# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import Rhino

count = 0
selected = rs.SelectedObjects()
# for obj in selected:
#     count += 1

if (selected):
    print(len(selected))

if len(selected) == 1 and rs.IsSurface(selected):
    print("got one")
    obj = selected
else:
    obj = rs.GetSurfaceObject("surface to porcupine-ify", select=True)

# ucount = rs.GetInteger("# of u points")
# vcount = rs.GetInteger("# of v points")

srfcurves = []
srfpoints = []
extensionpoints = []

rs.Command("_-ExtractIsocurve _Direction Both x !")
rs.Command("_Intersect")
# rs.Command("_SelNone")
# rs.Command("_SelCrv")
# rs.Command("_Hide")

srfpoints = rs.LastCreatedObjects()
for point in srfpoints:
    if point:
        param = rs.SurfaceClosestPoint(obj, point)
        normal = rs.SurfaceNormal(obj, param)
        extensionpoints.append(rs.AddPoints( [point, point + normal] ))


# for u in range(ucount):
#     for v in range(vcount):
#         srfcurves.append(rs.ExtractIsoCurve(obj, u, v))

#         SurfaceNormal
