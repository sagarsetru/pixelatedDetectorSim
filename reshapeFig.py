### python script to reshape an image text file into a single column array
### saves to a new text file
### Author: Sagar Setru

import sys, os, getopt
import numpy as np

myopts, args = getopt.getopt(sys.argv[1:],"i:o:h")
for o, a in myopts:
    if o == '-i':
        infile=a
    elif o == '-o':
        outfile=a
    elif o == '-h':
        print 'Usage:'
        print "-i <inputImage.txt> -o <outputColumn.txt>"
        sys.exit()

resize = 0
im1_original = np.loadtxt(infile)
im1 = im1_original
if resize == 1:
    im1 = im1[427:2689,813:3066]

im1size = im1.size

im1_column = im1.reshape((im1size,1))

inds = []
indcounter = 0
for entry in im1_column:
    if not np.isfinite(entry):
        print 'entry:'
        print entry
        print 'index of entry:'
        print indcounter
        inds += [indcounter]
    #print indcounter
    indcounter += 1
print 'inds'
print inds
im1_column_clean = np.delete(im1_column, inds)
np.savetxt(outfile,im1_column_clean)
