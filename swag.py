lines_seen = set() # holds lines already seen
swag = open("out.txt", "w")
for line in open("forgmaps.csv", "r"):
	
	if line not in lines_seen: # not a duplicate
        	swag.write(line)
        	lines_seen.add(line)
swag.close()
