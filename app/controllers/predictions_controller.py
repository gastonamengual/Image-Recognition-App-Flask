from ast import Mod
import io
from ..models.model import Model, ModelConfig
import numpy as np


def predict(image) -> str:

    in_memory_file = io.BytesIO()
    image.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)

    model = Model(ModelConfig)
    prediction = model.predict(data)

    return prediction


def real_time():
    model = Model(ModelConfig)
    model.real_time()
    return 1
