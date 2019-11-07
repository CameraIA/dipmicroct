x,_,_ = img.shape
IM_MEAN = img[0,:,:]
for M in np.arange(1,x):
    IM_MEAN = IM_MEAN + M //2
plt.imshow(IM_MEAN,vmin=0,vmax=255)
