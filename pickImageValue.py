### Python script that only keeps values in image matrix of particular value
### Saves image

import sys, os, getopt
import numpy as np
from scipy.misc import toimage
import matplotlib.pyplot as plt
import matplotlib.cm as cm

myopts, args = getopt.getopt(sys.argv[1:],"i:o:h")
for o, a in myopts:
    if o == '-i':
        infile=a
    elif o == '-o':
        outfile=a
    elif o == '-h':
        print 'Usage:'
        print "-i <inputImage.txt> -o <outputImage.txt>"
        sys.exit()

im_original = np.loadtxt(infile)
im_new = im_original
value = 1.00

countervalue = 0
counterrow = 0
for row in im_original:
    countercolumn = 0
    for entry in row:
        if  entry >= value and entry <= value+.016:
            countervalue += 1
        if  entry <= value or entry >= value+.016:
            im_new[counterrow,countercolumn] = 0
        countercolumn += 1
    counterrow += 1
#toimage(im_new).show()

print 'countervalue'
print countervalue

plt.imshow(im_new, cmap = cm.Greys_r)
plt.show()

