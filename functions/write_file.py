import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes contents to a specified file path, relative to the working directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema( 
                type=types.Type.STRING,
                description="The path to the target file, relative to the working directory.",
            ),
            "content": types.Schema( 
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    
    w_dir = os.path.abspath(working_directory)
    f_path = os.path.abspath(os.path.join(w_dir, file_path))

    if not f_path.startswith(w_dir + os.sep):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    f_path_dir = "/".join(f_path.split("/")[:-1])

    if not os.path.exists(f_path_dir):
        
        os.makedirs("/".join(f_path_dir)) 
    
    try:
        with open(f_path, 'w') as f:
            f.write(content)

    except Exception as e:
        return f"Error: {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'