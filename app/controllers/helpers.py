from .exceptions import NoImageSelected, WrongFilenameFormat


def validate_filename_exists(filename: str):
    if filename == "":
        raise NoImageSelected


def validate_filename_format(filename):
    allowed_extensions = ["png", "jpg", "jpeg"]
    if not "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions:
        raise WrongFilenameFormat
