### Python script that decomposes and input image into three image matrices
## One matrix is for Red
## One is for Green
## One is for Blue
## Author Sagar Setru

import sys, os, getopt
import numpy as np

from scipy.misc import imread

myopts, args = getopt.getopt(sys.argv[1:],"i:h")
for o, a in myopts:
    if o == '-i':
        infile=a
    elif o == '-h':
        print 'Usage:'
        print "-i <inputImage.JPG>"
        sys.exit()


imageIn = imread(infile)

imageOutRed = imageIn[:,:,0]
imageOutGreen = imageIn[:,:,1]
imageOutBlue = imageIn[:,:,2]

indsPeriod = [i for i in range(len(infile)) if infile.startswith('.', i)]
infileBase = infile[0:indsPeriod[len(indsPeriod)-1]]

np.savetxt(infileBase+'_Red.txt',imageOutRed)
print 'saving'+infileBase+'_Red.txt'
np.savetxt(infileBase+'_Green.txt',imageOutGreen)
print 'saving'+infileBase+'_Green.txt'
np.savetxt(infileBase+'_Blue.txt',imageOutBlue)
print 'saving'+infileBase+'_Blue.txt'

