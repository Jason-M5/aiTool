import os

def get_files_info(working_directory, directory="."):

    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(os.path.abspath(working_directory) + os.sep):
    
    #w_dir = os.path.abspath(working_directory + os.sep)
    #print(w_dir)
    #dir = os.path.join(w_dir, directory)
    #dir = os.path.abspath(dir)
    #if not dir.startswith(w_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    else:
        dir_contents = os.listdir(full_path)
        contents = []
        for i in dir_contents:
            f_path = os.path.join(full_path, i)
            contents.append(f'- {i}: file_size={os.path.getsize(f_path)} bytes, is_dir={os.path.isdir(f_path)}')
    
        return "\n".join(contents)

