from functions import get_files_info

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