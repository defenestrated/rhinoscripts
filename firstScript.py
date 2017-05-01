# add some points to Rhino using the rhinoscript package
import rhinoscript
count = rhinoscript.userinterface.GetInteger("Number of points")
if count:
    for i in range(count):
        x = i
        y = i
        if( i > count/2 ): y = count-i
        rhinoscript.geometry.AddPoint([x,y,0])