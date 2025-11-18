import os
import subprocess 
from google.genai import types
from config import *


def run_python_file(working_directory, file_path, args=[]):
    joined = os.path.join(working_directory,file_path)
    full = os.path.abspath(joined)
    root = os.path.abspath(working_directory)

    # print(joined, full, root)

    if os.path.commonpath([full, root]) != root: #questo si può verificare quando directory è ".." perchè nel caso usciamo dalla cartella 
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.isabs(file_path) or file_path.startswith('~'):   
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        # timeout = TIMEOUT
        command  = ["uv","run",full]
        if args:
            command.extend(args)
        result = subprocess.run(command,
                                timeout=TIMEOUT,
                                capture_output=True)

        
        return_string = f"STDOUT:{result.stdout}\n STDERR:{result.stderr}"
        if result.returncode != 0:
            return_string + f"\nProcess exited with code {result.returncode}"

        if not result.stdout:
            return f"No output produced"+return_string

        return return_string 
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    # subprocess.run(["uv","run",f"{file_path}",args],timeout=timeout,capture_output=True)
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python script, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the script to run, relative to the working directory. If not provided, raises an exception",
            ),
            "args": types.Schema(
                type = types.Type.STRING,
                description="the positional arguments fro the script. If not provided the script is run without any positional arguments"
            )
        },
    ),
)