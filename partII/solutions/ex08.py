#return largest connected component
def getLargestCC(segments):
        '''Return a mask corresponding to the largest object'''
        labels = label(segments.astype('int'),connectivity=1)
        largestCC = labels == np.argmax(np.bincount(labels.flat, weights=segments.flat))
        return largestCC

a=getLargestCC(binary)

print('Volume largest obj: '+str(np.count_nonzero(a)))
print('Volume dense phase: '+str(np.count_nonzero(binary)))
