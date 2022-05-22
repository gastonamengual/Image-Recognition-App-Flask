import io
from ..models.model import Model, ModelConfig
from .helpers import validate_filename_exists, validate_filename_format
import numpy as np

from werkzeug.datastructures import FileStorage


def detect_object(image_file: FileStorage) -> str:

    image_filename: str = image_file.filename
    validate_filename_exists(image_filename)
    validate_filename_format(image_filename)

    in_memory_file = io.BytesIO()
    image_file.save(in_memory_file)
    image = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)

    model = Model(ModelConfig)
    output_filename = model.detect_object(image)

    return output_filename


# def real_time():
#     model = Model(ModelConfig)
#     model.real_time()
#     return 1
