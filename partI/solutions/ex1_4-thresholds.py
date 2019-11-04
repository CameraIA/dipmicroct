filters.try_all_threshold(plane_denoised, figsize=(8, 14))

print('\n')
print('* ISODATA threshold: {}'.format(filters.threshold_isodata(plane_denoised)))  # This one is for free!
print('* Li threshold: {}'.format(filters.threshold_li(plane_denoised)))  # Li
print('* Mean threshold: {}'.format(filters.threshold_mean(plane_denoised)))  # Mean
print('* Minimum threshold: {}'.format(filters.threshold_minimum(plane_denoised)))  # Minimum
print('* Otsu threshold: {}'.format(filters.threshold_otsu(plane_denoised)))  # Otsu
print('* Triangle threshold: {}'.format(filters.threshold_triangle(plane_denoised)))  # Triangle
print('* Yen threshold: {}'.format(filters.threshold_yen(plane_denoised)))  # Yen
