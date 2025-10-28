import os
from config import *

def get_files_contents(working_directory, file_path):
    try:
        wd_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(wd_abs, file_path))

        if not full_path.startswith(wd_abs + os.sep) or full_path == wd_abs:
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(full_path):
            return(f'Error: File not found or is not a regular file: "{file_path}"')
        with open(full_path, "r") as f:
            file_contents = f.read(MAX_CHARS)
            if len(file_contents) >= MAX_CHARS:
                return f'{file_contents}[...File "{file_path}" truncated at 10000 characters]'
            return file_contents



    except Exception as e:
        return f"Error: {e}"

