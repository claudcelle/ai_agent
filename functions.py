import os
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



# print(get_files_info('calculator'))
