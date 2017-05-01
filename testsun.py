import rhinoscriptsyntax as rs
numberofpoints = rs.GetInteger("how many points?")
radius = rs.GetReal("what's the radius?")

rs.AddLayer("Sphere", [255,0,0])
rs.CurrentLayer("Sphere")

Sunsphere = rs.AddSphere([0,0,0], radius)

if ((numberofpoints > 0) and (radius > 0)):
    #stuff if true
    print "we're good"
    
    dayname = rs.GetString("what day is this?")
    print "the entered day name is:", dayname
    
    rs.AddLayer(dayname, [0,0,255])
    rs.CurrentLayer(dayname)
    
    listofpoints = []
    
    startpoint = rs.AddPoint([0,radius,0])
    
    for i in range(numberofpoints):
        elevation = rs.GetReal("what's the elevation?")
        azimuth = rs.GetReal("what's the azimuth?")
        azimuth *= -1
        rs.RotateObject (startpoint, [0,0,0], elevation, axis=[1,0,0], copy=True)
        rs.RotateObject (rs.FirstObject(), [0,0,0], azimuth, axis=[0,0,1], copy=False)
        
        listofpoints.append(rs.FirstObject())
    
    sunpath = rs.AddInterpCurve(listofpoints)
    
    
    
    
    
    
else:
    #stuff if not true
    print "please enter a real number above zero"