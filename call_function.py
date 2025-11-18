from google.genai import types

from functions.get_files_info import *
from functions.get_file_content import *
from functions.run_python_file import *
from functions.write_file import *

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part,verbose = False):
    name = function_call_part.name
    args = function_call_part.args
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    kwargs = {'working_directory':"./calculator"}
    for k in ("file_path", "directory", "content"):
        if k in args:
            # print(f"{k}: {args[k]}")
            kwargs[k] = args[k]

    result = name()

    