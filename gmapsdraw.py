import pygmaps
f = open('forgmaps.csv', 'r')
mymap = pygmaps.maps(0, 0, 3)
 

for line in f:
        linestrip = line.strip()
        print linestrip	

	words = linestrip.split()
	try:	
        	latitude = float(words[1])
        	longitude = float(words[2])
        	mymap.addpoint(latitude, longitude, "#0000FF")
	except:
		pass
        #print latitude
        #print longitude
#it's lat long then colour then ip      
    

mymap.draw('./mymap22.html')