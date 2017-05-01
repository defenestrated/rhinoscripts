import rhinoscriptsyntax as rs
point1 = rs.GetPoint("Pick first point")
if point1:
    rs.AddPoint(point1)
    point2 = rs.GetPoint("Pick second point", point1)
    if point2:
        rs.AddPoint(point2)
        distance = (point1-point2).Length
        point3 = rs.GetPoint("Pick third point", point2, distance)
        if point3: rs.AddPoint(point3)