import os, shutil

# NOTE: You can write every single extensions inside tuples

dict_extensions = {

    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'Document_extensions' : ('.doc', '.pdf', '.txt'),
    'MsWord_extension' : ('.docx','.doc'),
    'MsXL_extension'   : ('.xlsx','.xl'),
    'Image_extensions'  : ('.jpg','.png'),
    'Software_extensions' : ('.xex',".exe"),
    'Zip_extensions' : ('.zip', '.zep')
}

folderpath = input('Enter Folder Path : ')

def file_finder(folder_path, file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files
for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] +' '+'Folder'
    folder_path = os.path.join(folderpath, folder_name)
    if os.path.exists(folder_path):
         for item in file_finder(folderpath, extension_tuple):
            item_path = os.path.join(folderpath,item)
            item_new_path = os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)
        
    else :
        os.mkdir(folder_path)
        for item in file_finder(folderpath, extension_tuple):
            item_path = os.path.join(folderpath,item)
            item_new_path = os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)


    







