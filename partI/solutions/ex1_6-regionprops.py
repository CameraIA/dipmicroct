cells_conv_areas = [prop.convex_area for prop in properties]
cells_orientation = [prop.orientation for prop in properties]

print('Convex areas: {}'.format(cells_conv_areas))
print('Orientation: {}'.format(cells_orientation))
