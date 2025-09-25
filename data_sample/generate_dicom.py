import pydicom
from pydicom.dataset import Dataset, FileDataset
import numpy as np
import os, datetime

os.makedirs("data_sample", exist_ok=True)

def create_dicom(filename):
    file_meta = Dataset()
    ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0" * 128)
    ds.PatientName = "Test^Patient"
    ds.PatientID = "123456"

    # Data/hora
    dt = datetime.datetime.now()
    ds.ContentDate = dt.strftime("%Y%m%d")
    ds.ContentTime = dt.strftime("%H%M%S")

    # Imagem fake
    arr = np.random.randint(0, 256, (256, 256), dtype=np.uint16)
    ds.Rows, ds.Columns = arr.shape
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.SamplesPerPixel = 1
    ds.BitsStored = 16
    ds.BitsAllocated = 16
    ds.HighBit = 15
    ds.PixelRepresentation = 1
    ds.PixelData = arr.tobytes()

    ds.save_as(filename)

# Gerar 10 arquivos de exemplo
for i in range(10):
    create_dicom(f"data_sample/sample_{i}.dcm")

print("Arquivos DICOM sintéticos gerados em data_sample/")
