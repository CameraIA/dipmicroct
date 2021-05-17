x,_,_ = img.shape
IM_MEAN = img[0,:,:]/x
for M in np.arange(1,x):
    IM_MEAN = IM_MEAN + img[M,:,:]/x
plt.imshow(IM_MEAN,vmin=np.min(IM_MEAN),vmax=np.max(IM_MEAN))
