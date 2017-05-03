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
    print("number of objects selected: " + str(len(selected)))

if len(selected) == 1 and rs.IsSurface(selected):
    print("got one")
    obj = selected
else:
    print("don't got one")
    obj = rs.GetSurfaceObject("surface to porcupine-ify", select=True)

print(obj)

scale = rs.GetReal("distance away from surface", 1)

# ucount = rs.GetInteger("# of u points")
# vcount = rs.GetInteger("# of v points")

srfcurves = []
srfpoints = []
extensionpoints = []
extensionlines = []
srfcircles = []
extcircles = []

rs.Command("_-ExtractIsocurve _Direction Both x !")
srfcurves = rs.LastCreatedObjects()
rs.Command("_Intersect")
# rs.Command("_SelNone")
# rs.Command("_SelCrv")
# rs.Command("_Hide")

pile = rs.LastCreatedObjects()
for thing in pile:
    if rs.ObjectType(thing) != 1:
        rs.UnselectObject(thing)

srfpoints = rs.SelectedObjects()

# print("obj", obj)
# print(srfpoints)

for point in srfpoints:
    pt = rs.coerce3dpoint(point)
    if point:
        param = rs.SurfaceClosestPoint(obj, pt)
        normal = rs.SurfaceNormal(obj, param) * scale
        outlier = rs.AddPoint(pt + normal)
        extensionpoints.append(outlier)
        extensionlines.append(rs.AddLine(pt, outlier))
        srfcircles.append(rs.AddCircle(pt, 0.1))
        extcircles.append(rs.AddCircle(outlier, 0.1))

def layer(name):
    if rs.IsLayer(name):
        return name
    else:
        if name != "porcupines":
            return rs.AddLayer(name, parent="porcupines")
        else:
            return rs.AddLayer(name)


layer("porcupines")

for point in srfpoints:
    rs.ObjectLayer(point, layer=layer("surface_points"))
for c in srfcircles:
    rs.ObjectLayer(c, layer=layer("surface_points"))

for point in extensionpoints:
    rs.ObjectLayer(point, layer=layer("extension_points"))
for c in extcircles:
    rs.ObjectLayer(c, layer=layer("extension_points"))

for line in extensionlines:
    rs.ObjectLayer(line, layer=layer("extension_lines"))
for curve in srfcurves:
    rs.ObjectLayer(curve, layer=layer("surface_curves"))
