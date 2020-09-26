import logging
from pathlib import Path

dateformat = "%Y-%m-%d %H:%M:%S"

def get_handlers(log_directory):
    if not isinstance(log_directory, Path):
        log_directory = Path(log_directory)
    if not log_directory.exists():
        log_directory.mkdir(exist_ok = True)
    
    debug_file_handler = logging.FileHandler(log_directory / "debug.log", mode = "w")
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = dateformat)
    debug_file_handler.setFormatter(debug_file_formatter)

    app_file_handler = logging.FileHandler(log_directory / "app.log", mode = "w")
    app_file_handler.setLevel(logging.INFO)
    app_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = dateformat)
    app_file_handler.setFormatter(app_file_formatter)

    error_file_handler = logging.FileHandler(log_directory / "error.log", mode = "w")
    error_file_handler.setLevel(logging.ERROR)
    error_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = dateformat)
    error_file_handler.setFormatter(error_file_formatter)

    return (debug_file_handler, app_file_handler, error_file_handler,)