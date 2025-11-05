import os
from google.genai import types
from config import *

def get_file_content(working_directory,file_path):

    joined = os.path.join(working_directory,file_path)
    full = os.path.abspath(joined)
    root = os.path.abspath(working_directory)

    # print(joined, full, root)

    if os.path.commonpath([full, root]) != root: #questo si può verificare quando directory è ".." perchè nel caso usciamo dalla cartella 
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if os.path.isabs(file_path) or file_path.startswith('~'):   
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full):
        return f'Error: File not found or is not a regular file: "{file_path}"'
     

    try:
        with open(full, "r") as f:
            # file_content_string = f.read()
            file_content_string = f.read(MAX_CHARS)
    
        # if len(file_content_string) > MAX_CHARS:
        if os.path.getsize(full) > MAX_CHARS:
            return file_content_string[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'            
        else:
            return file_content_string   
    except Exception as e:
        return f"Error: {e}" 


