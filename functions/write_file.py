import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
        valid_target = os.path.commonpath([working_dir_abs_path, target_file]) == working_dir_abs_path

        if not valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file relative to the working directory, creating the file and any missing parent directories, and overwriting the file if it already exists",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The full text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
