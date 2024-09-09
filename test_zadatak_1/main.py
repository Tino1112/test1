import rasterio
import numpy as np

input_file = r'C:\Users\User\PycharmProjects\test_zadatak_1\response_bands.tiff'

with rasterio.open(input_file) as src:
    band_count = src.count
    print(f"Satelitska snimka sadrži {band_count} kanala.")

    red_band = src.read(4).astype('float32')  # Pretpostavljamo da je band 4 RED
    nir_band = src.read(8).astype('float32')  # Pretpostavljamo da je band 8 NIR

    ndvi = (nir_band - red_band) / (nir_band + red_band)
    ndvi = np.nan_to_num(ndvi, nan=0.0)

    swir_band = src.read(11).astype('float32')

    ndmi = (nir_band - swir_band) / (nir_band + swir_band)
    ndmi = np.nan_to_num(ndmi, nan=0.0)

    ndvi_output_file = 'ndvi_output.tiff'
    with rasterio.open(
            ndvi_output_file,
            'w',
            driver='GTiff',
            height=ndvi.shape[0],
            width=ndvi.shape[1],
            count=1,
            dtype='float32',
            crs=src.crs,
            transform=src.transform
    ) as dst:
        dst.write(ndvi, 1)

    ndmi_output_file = 'ndmi_output.tiff'
    with rasterio.open(
            ndmi_output_file,
            'w',
            driver='GTiff',
            height=ndmi.shape[0],
            width=ndmi.shape[1],
            count=1,
            dtype='float32',
            crs=src.crs,
            transform=src.transform
    ) as dst:
        dst.write(ndmi, 1)

    ndvi_mean = np.mean(ndvi)
    ndmi_mean = np.mean(ndmi)
    print(f"Prosječna vrijednost NDVI-a: {ndvi_mean:.4f}")
    print(f"Prosječna vrijednost NDMI-a: {ndmi_mean:.4f}")

