import zipfile

# create a zip file
# the new file created is called files.zip
# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('test.txt')
#     my_zip.write('Allouch-Dad.png')

with zipfile.ZipFile('files.zip', 'r') as my_zip:
    print(my_zip.namelist())
    # extract all files into a new directory called "myDirectory"
    # my_zip.extractall('myDirectory')

    # extract one file into a new directory called "myDirectory"
    my_zip.extract('Allouch-Dad.png')
