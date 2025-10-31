import os
import subprocess 
from config import *

def get_files_info(working_directory, directory="."):

    joined = os.path.join(working_directory,directory)
    full = os.path.abspath(joined)
    root = os.path.abspath(working_directory)

    # print(joined, full, root)

    if os.path.commonpath([full, root]) != root: #questo si può verificare quando directory è ".." perchè nel caso usciamo dalla cartella 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isabs(directory) or directory.startswith('~'):   
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
 
    if not os.path.isdir(full):
        return f'Error: "{directory}" is not a directory'
    
    # print(os.listdir(full))
    try:
        res = []
        for name in os.listdir(full):      
            path = os.path.join(full, name)      
            row = f"- {name}: file_size={os.path.getsize(path)} bytes, is_dir={os.path.isdir(path)}"
            res.append(row+"\n")
    except Exception as e:
        return f"Error: {e}"
    return ''.join(res)




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
            file_content_string = f.read()
    
        if len(file_content_string) > MAX_CHARS:
            return file_content_string[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'
        else:
            return file_content_string   
    except Exception as e:
        return f"Error: {e}" 



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
        command.extend(args)
        result = subprocess.run(command,timeout=TIMEOUT,capture_output=True)

        
        return_string = f"STDOUT:{result.stdout}\n STDERR:{result.stderr}"
        if result.returncode != 0:
            return_string + f"\nProcess exited with code {result.returncode}"

        if not result.stdout:
            return f"No output produced"+return_string

        return return_string 
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    # subprocess.run(["uv","run",f"{file_path}",args],timeout=timeout,capture_output=True)
    
# print(get_files_info('calculator'))
# print(get_file_content('))


# write_file('.','provamario')