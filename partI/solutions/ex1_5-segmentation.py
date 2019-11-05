smooth_distance = filters.median(plane_distance,
                                 selem=morphology.disk(20))
peak_local_max = feature.peak_local_max(
    smooth_distance,
    footprint=np.ones((20, 20), dtype=np.bool),
    indices=False,
    labels=measure.label(plane_remove_objects)
)

plane_markers = measure.label(peak_local_max)

plane_labels = morphology.watershed(
    plane_rescaled,
    plane_markers,
    mask=plane_remove_objects
)

# Checking the results.
_, (win_left, win_right) = plt.subplots(nrows=1, ncols=2, figsize=(12, 8))

sc.show_plane(win_left, plane, title='Original')
sc.show_plane(win_right, plane_labels, cmap='nipy_spectral', title='Watershed labels')
