import io
from ..models.model import Model
import numpy as np


def predict(image) -> str:

    in_memory_file = io.BytesIO()
    image.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)

    model = Model()
    prediction = model.predict(data)

    return prediction
