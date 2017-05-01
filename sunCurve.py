import rhinoscriptsyntax as rs
# this pulls in all of rhino's native commands into python,
# so from here on out we can just say rs.[whatever] to access rhino's stuff
# a list of rhino python commands is here: http://www.rhino3d.com/5/ironpython/index.html
# first, we need some information from the user:
numDays = rs.GetInteger("how many days (or curves)?") # store the number of days into a variable called numDays
numPts = rs.GetInteger("how many data points per day?") # do the same for the number of data points
radius = rs.GetInteger("what's the radius of your sun-sphere?") # get a radius for the sphere the sun's going to rotate around
rs.AddLayer("sunSphere") # make a new layer for the sphere itself
rs.CurrentLayer("sunSphere") # go to that layer
sunSphere = rs.AddSphere([0,0,0], radius) # draw the sunsphere (and store it in a variable called sunSphere)



# saying if(something) is the same as saying if(something is not nothing) -
# it just checks to see whether there's anything non-zero in all these variables
if (numDays and numPts and radius):


    # this next thing is called a 'for loop' - it basically says:
    # - make a variable called 'i' which starts at 0
    # - as long as i is less than numDays, do whatever follows.
    # - when you're done with the block of code, add 1 to i.
    # so a for loop is a great way to do something repeatedly a specific number of times
    # (i.e. until i is no longer less than numDays)
    # in our case, we're using first the days, and then the data points, as 'how many times to loop'
    
    # so: cycle through each day, and each time, do the following
    for i in range(numDays):
        dayName = rs.GetString("which day is this? (no spaces!)") # ask for a label for the eventual curve object
        print "dayName = ", dayName # print it to the command line, just to make sure it worked
        rs.AddLayer(dayName, [255,255,255]) # make a new layer for each day - make everything on them white, just to distinguish
        # (you can change [255,255,255] to any color, or delete that part)
        rs.CurrentLayer(dayName) # go to that layer
        dataPts = [] # setup a list (empty at this point) to hold all the points for the curve
        rs.AddPoint([0,radius,0]) # put down one point at x=0, y= the radius of the sun-sphere, z=0
        starterPt = rs.FirstObject() # FirstObject grabs the last thing created - let's name that 'starterPt'
        
        
        # each day has a set of data points, so now we're going through each individual point
        for i in range (numPts):
            elevation = rs.GetInteger("what's the elevation angle?") # ask for an elevation angle, just like up top
            azimuth = rs.GetInteger("what's the azimuth angle?") # ask for an azimuth angle
            
            if ((azimuth != None) and (elevation != None)): # if we a
                azimuth *= -1 # flip the azimuth - because by default, rhino rotates things CCW, and compasses go CW
                # rotate that first point to the elevation angle
                # rotate works like this: RotateObject( object_to_rotate, center_point, angle_to_rotate, rotation_axis, copy_yes/no )
                rs.RotateObject(starterPt, [0,0,0], elevation, axis=[1,0,0], copy=True)
                rs.RotateObject(rs.FirstObject(), [0,0,0], azimuth, axis=[0,0,1], copy=False) # do the same thing for the azimuth
                dataPts.append(rs.FirstObject()) # once we have the final location, add that point to our dataPts list
            else: # this happens if we didn't get an elevation or azimuth
                print "please enter both elevation and azimuth" # print an explanation
                break # exit the 'for loop'
                
                
        if(dataPts): # check whether dataPts has anything in it
             sunpath = rs.AddInterpCurve(dataPts) # add an interpolated curve (one that goes THROUGH the points)
             newsunpath = rs.PullCurve(sunSphere, sunpath, False) # pull that curve to the sphere
             rs.ObjectName(newsunpath, dayName) # name it using the 'dayName' variable from earlier
             rs.DeleteObject(sunpath) # delete the old (non-pulled) curve
             crvstojoin = rs.ObjectsByName(dayName, True) # sometimes pulling breaks up a curve, so we have to gather all those pieces
             if (len(crvstojoin) > 1): # if, in fact, there are multiple curves
	             joined = rs.JoinCurves(crvstojoin, True) # join them
             rs.ObjectName(joined, dayName) # for some reason joining things kills their names - so rename the final curve
             rs.DeleteObject(starterPt) # finally, delete that original point that we copied and rotated around
             
else: # if we didn't successfully get days, points, or radius
    print "please enter non-zero values!" # explain why nothing happened