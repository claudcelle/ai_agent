import os
from google.genai import types
from config import *


def write_file(working_directory, file_path, content):

    joined = os.path.join(working_directory,file_path)
    full = os.path.abspath(joined)
    root = os.path.abspath(working_directory)

    # print(joined, full, root)

    if os.path.commonpath([full, root]) != root: #questo si può verificare quando directory è ".." perchè nel caso usciamo dalla cartella 
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if os.path.isabs(file_path) or file_path.startswith('~'):   
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full):
        print(f'File not found or is not a regular file: "{file_path}"')
        print(f'Created file: "{file_path} at {working_directory}"')

        try: 
            with open(full,'w') as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return e
    else:
        print(f"File exists, overwriting...")
        try: 
            with open(full,'w') as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return e


