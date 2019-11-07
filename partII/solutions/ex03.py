from skimage.filters.rank import mean_bilateral
from skimage.morphology import disk

bilat = np.empty_like(img)
for i, aslice in enumerate(img):
    bilat[i] = mean_bilateral(aslice.astype(np.uint8), disk(3), s0=15, s1=15)

slicing(img,'gray')    
