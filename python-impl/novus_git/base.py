from pathlib import Path
import os
from . import data
'''
We perform a DFS-like search to recursively find and list the files and folders
present inside the directory.
'''

def write_tree(directory="."):
    with os.scandir(directory) as it:
        for entry in it:
            full = os.path.join(directory,entry.name)
            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                '''
                Here we are not only printing the filename but the associated OID however this is only a makeshift solution as we are not printing the OID that represents the directory but the individual OID of files whoch is not useful and any file that is not in the object database, their names are printed instead of any OID as OID is only for Object database in a version control system 
                '''
                with open(full, 'rb') as f:
                    print(data.hash_object(f.read()),full)
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full) 


'''
the below function is used for ignoring the files that are present inside the .novus_git
directory
'''
def is_ignored(path):
    return ".novus_git" in path.split('/')
