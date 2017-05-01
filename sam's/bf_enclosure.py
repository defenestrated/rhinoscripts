# use rhinoscriptsyntax to get all the functions in one shot
import rhinoscriptsyntax as rs
import random
import time
import Rhino

def main():

    cyls = []
    radius = 0

    gname = "Enclosure"

    extantGroups = rs.GroupNames();
    print "groups: ", extantGroups
    enclosures = [s for s in extantGroups if "Enclosure" in s]
    print "enclosures: ", enclosures

    if rs.IsGroup("Enclosure"):
    	num = len(enclosures)
        gname += "_" + `num`
    encGroup = rs.AddGroup(gname)
    print "group: ", encGroup

    focus = rs.GetPoint("center of fence")
    if (focus is None): return
    rpt = rs.GetPoint("enclosure radius", focus)
    if (rpt is None): return
    else:
        radius = (rpt - focus).Length
        rs.AddObjectsToGroup(rs.AddCircle(focus, radius), encGroup)

    count = rs.GetInteger("number of cylinders")
    if (count is None): return
    cyldiam = rs.GetReal("cylinder diameter")
    if (cyldiam is None): return
    minheight = rs.GetReal("minimum height")
    if (minheight is None): return
    maxheight = rs.GetReal("maximum height")
    if (maxheight is None): return
#   arcjitter = rs.GetReal("amount of arc jitter")
#   if (arcjitter is None): return
#   radialjitter = rs.GetReal("amount of radial jitter")
#   if (radialjitter is None): return



    for i in range(count):
        cyl = rs.AddCylinder(rpt, random.uniform(minheight, maxheight), cyldiam/2, True)
        rs.RotateObject(cyl, focus, (360/count)*(i+1))
        cyls.append(cyl)
    if cyls: rs.AddObjectsToGroup(cyls, encGroup)
    print "Enclosure built:"
    print "focus: (", focus, ")"
    print "radius:", radius
    print "cylinders:", count, "ranging from", minheight, "to", maxheight, "units in length."

main()