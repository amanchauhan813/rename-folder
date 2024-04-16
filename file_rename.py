import os

def rename_files(directory, pattern):
    files = os.listdir(directory)
    
    for filename in files:
        old_path = os.path.join(directory, filename)
        
        file_ext = os.path.splitext(filename)[1]
        
        new_filename = pattern.format(filename=filename, ext=file_ext)
        
        new_path = os.path.join(directory, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")


directory = r'C:\Users\amanc\Desktop\python new project\New folder'
pattern = "{filename}_new{ext}"  

rename_files(directory, pattern)
