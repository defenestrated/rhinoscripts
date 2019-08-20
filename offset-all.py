import rhinoscriptsyntax as rs


def offsetcurves():
    alreadyselected = rs.SelectedObjects()

    if alreadyselected:
        objs = alreadyselected
    else:
        objs = rs.GetObjects("pick curves to offset")

    if not objs: return

    dist = rs.GetReal("offset distance")
    if dist == None: return

    innieoutie = rs.GetBoolean("offset direction", ("direction", "innie", "outie"), False)
    # innie = false, outie = true
    print "doing an", "outie" if innieoutie[0] else "innie", "offset"
    print "attempting to offset ", len(objs), " objects"

    for obj in objs:

        if rs.IsCurve(obj):
            print rs.ObjectName(obj)
            center = rs.CurveAreaCentroid(obj) # get centroid

            if innieoutie[0] == False: # innie
                rs.OffsetCurve(obj, center[0], dist)
            elif innieoutie[0] == True:
                end = rs.CurveEndPoint(obj) # get end
                pt = rs.AddPoint(end) # add temporary point
                rs.MoveObject(pt, end-center[0]) # move it outside the circle
                if pt:
                    # rs.ObjectName(pt, "point-" + rs.ObjectName(obj))
                    rs.OffsetCurve( obj, pt, dist) # use temporary point for offset direction
                    rs.DeleteObject(pt)

offsetcurves()
