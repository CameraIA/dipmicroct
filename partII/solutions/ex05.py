#Transform raw image into a morphologically dilated one, using grayscale dilation 
gdil = ndi.grey_dilation(img,footprint=aball)
slicing(gdil,'gray')
