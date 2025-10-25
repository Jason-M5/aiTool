import os

def get_files_info(working_directory, directory="."):
    try:
        wd_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(wd_abs, directory))

        if not (full_path.startswith(wd_abs + os.sep) or full_path == wd_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        lines = []
        for name in os.listdir(full_path):
            p = os.path.join(full_path, name)
            size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
            lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"

