from PIL import Image
import sys

import re
splitDescription = re.compile(r'''(\d+)(n|s)(\d+)(e|w)''')

squaresize = int(sys.argv[1])

maxNorth = 13
maxSouth = 19
maxEast = 48
maxWest = 33

height = (maxNorth + maxSouth)*squaresize
width = (maxEast + maxWest)*squaresize

print height, width, height*width


def findTopLeft(description):
	(verticalTiles, ns, horizontalTiles, ew) = splitDescription.search(description).groups()
	verticalTiles = int(verticalTiles)
	horizontalTiles = int(horizontalTiles)

	if ns == "n":
		top = maxNorth - verticalTiles
	elif ns == "s":
		top = maxNorth + verticalTiles -1
	if ew == "w":
		left = maxWest - horizontalTiles
	elif ew == "e":
		left = maxWest + horizontalTiles -1

	return (left*squaresize, top*squaresize)



merge = Image.new("L", (width, height), "grey")

for imgFile in sys.argv[2:]:
	img = Image.open(imgFile)
	if img.size != (squaresize, squaresize):
		img = img.resize((squaresize, squaresize))
	topleft = findTopLeft(imgFile)
	merge.paste(img, topleft)


merge.save("merge_%sx%s.png" % (squaresize, squaresize))

