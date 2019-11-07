from skimage.measure import label
labeled = label(binary.astype('int'),connectivity=2)
print(np.max(labeled))

def slicer(z):
    plt.imshow(labeled[z,::downsample,::downsample], cmap='rainbow')

interact(slicer, z=IntSlider(min=0, max=len(img), step=1, value=68));
