from functions.get_files_info import *

print("Result for current directory:")
res = get_files_info("calculator", ".")
print(res)

print("\nResult for 'pkg' directory:")
res = get_files_info("calculator", "pkg")
print(res)

print("\nResult for '/bin' directory:")
res = get_files_info("calculator", "/bin")
print(res)

print("\nResult for '../' directory:")
res = get_files_info("calculator", "../")
print(res)

# --- o --- o --- o --- ## 
from functions.get_file_content import *

print('Result for "lorem.txt":')
res = get_file_content("calculator", "lorem.txt")
print(res)

print('\nResult for "main.py":')
res = get_file_content("calculator", "main.py")
print(res)

print('\nResult for "pkg/calculator.py":')
res = get_file_content("calculator", "pkg/calculator.py")
print(res)

print('\nResult for "/bin/cat":')
res = get_file_content("calculator", "/bin/cat")
print(res)

print('\nResult for "pkg/does_not_exist.py":')
res = get_file_content("calculator", "pkg/does_not_exist.py")
print(res)

# --- o --- o --- o --- ## 
from functions.write_file import *


print('Result for "lorem.txt":')
res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(res)

print('\nResult for "pkg/morelorem.txt":')
res = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(res)

print('\nResult for "/tmp/temp.txt":')
res = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(res)


## --- o --- o --- o --- ## 
from functions.run_python_file import *

print('Result for "main.py" (usage instructions):')
res = run_python_file("calculator", "main.py")
print(res)

print('\nResult for "main.py" with ["37 + 523"] (calculator run):')
res = run_python_file("calculator", "main.py", ["37 + 523"])
print(res)

print('\nResult for "tests.py":')
res = run_python_file("calculator", "tests.py")
print(res)

print('\nResult for "../main.py" (should error):')
res = run_python_file("calculator", "../main.py")
print(res)

print('\nResult for "nonexistent.py" (should error):')
res = run_python_file("calculator", "nonexistent.py")
print(res)

print('\nResult for "lorem.txt" (should error):')
res = run_python_file("calculator", "lorem.txt")
print(res)
