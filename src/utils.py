import pydicom
import numpy as np

def process_dicom(filepath):
    ds = pydicom.dcmread(filepath)

    # Anonimização básica
    if "PatientName" in ds:
        ds.PatientName = "ANONYMIZED"
    if "PatientID" in ds:
        ds.PatientID = "0000"

    # Compressão simulada
    pixel_array = ds.pixel_array.astype(np.float32)
    compressed = pixel_array[::2, ::2]  # downsample

    # Estatísticas
    stats = {
        "file": filepath,
        "shape": compressed.shape,
        "mean": float(np.mean(compressed)),
        "std": float(np.std(compressed)),
    }
    return stats
