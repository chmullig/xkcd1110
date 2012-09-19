import urllib

imageURLS = []

class MyIMGopener(urllib.FancyURLopener):
    def http_error_default(self, url, fp, errcode, errmsg, headers):
        if errcode == 404:
            raise IOError

imgretrieve = MyIMGopener()

maxn = 0
maxs = 0
maxe = 0
maxw = 0

for i in xrange(0, 55):
    for j in xrange(0, 55):
        for ns in ["n", "s"]:
            for ew in ["e", "w"]:
                success=False
                img = "http://imgs.xkcd.com/clickdrag/%s%s%s%s.png" % (i, ns, j, ew)
                try:
                    imgretrieve.retrieve(img, img.split("/")[-1])
                    success = True
                except IOError:
                    print "404 on %s" % img
                    pass
                if ns == "n" and i > maxn:
                    maxn = i
                if ns == "s" and i > maxs:
                    maxs = i
                if ew == "e" and i > maxe:
                    maxe = j
                if ew == "w" and i > maxw:
                    maxw = j

print "Max N: ", maxn
print "Max S: ", maxs
print "Max E: ", maxe
print "Max W: ", maxw