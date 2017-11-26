import os
def rename_files():
    file_list = os.listdir(r"E:\Programing\Python\CS102\secret_message\prank")
    # return file_list
    cwd = os.getcwd()
    os.chcwd(r"E:\Programing\Python\CS102\secret_message\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chcwd(cwd)
    return "Files were renamed"

print rename_files ()
