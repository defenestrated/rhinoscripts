import rhinoscriptsyntax as rs

def main():
    counts = [0,0,0]
    spacings = [10,10,10]
    rotations = [0,0,0]

    counts[0] = rs.GetInteger("number in x direction", minimum=1)
    # counts[1] = rs.GetInteger("number in y direction", minimum=1)
    # counts[2] = rs.GetInteger("number in z direction", minimum=1)

    spacings[0] = rs.GetReal("x spacing")
    # spacings[1] = rs.GetReal("y spacing")
    # spacings[2] = rs.GetReal("z spacing")

    rotations[0] = rs.GetReal("rotation of each object along x axis")
    # rotations[1] = rs.GetReal("y spacing")
    # rotations[2] = rs.GetReal("z spacing")


    print "count", counts
    print "spacing", spacings
    print "rotation", rotations

    for ix in range(counts[0]):
        newobj = rs.CopyObject(obj, [spacings[0]*ix, 0, 0])
        bbox = rs.BoundingBox(newobj)
        if bbox:
            centroid = rs.PointSubtract(bbox[0], bbox[6])
            print bbox[6], bbox[0]
            print centroid
            rs.AddPoint(centroid)
        else: print "no bbox"

        # rs.RotateObject(newobj, )



obj = rs.GetObject()

if obj:
    ot = rs.ObjectType(obj)
    print(ot)

    if ot == 4 or 8 or 16 or 32: # crv, srf, polysrf, mesh
        # if ot == 4: #curve
            # cent =
        main()
    else: rs.MessageBox("incompatible object type (works only with curves, surfaces, polysurfaces, meshes)")
