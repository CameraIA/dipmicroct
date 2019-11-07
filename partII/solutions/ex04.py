from skimage.filters.rank import enhance_contrast

contr = np.empty_like(img)
for i, aslice in enumerate(img):
    contr[i]= enhance_contrast(aslice.astype(np.uint16),disk(3))
slicing(contr,'gray')
