from pathlib import Path
import os
from . import data
'''
We perform a DFS-like search to recursively find and list the files and folders
present inside the directory.
'''

def write_tree(directory="."):
    entries = []
    with os.scandir(directory) as it:
        for entry in it:
            full = os.path.join(directory,entry.name)
            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                type_ = 'blob'
                '''
                Here we are not only printing the filename but the associated OID however this is only a makeshift solution as we are not printing the OID that represents the directory but the individual OID of files whoch is not useful and any file that is not in the object database, their names are printed instead of any OID as OID is only for Object database in a version control system 
                '''
                with open(full, 'rb') as f:
                    oid = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = 'tree'
                oid = write_tree(full)
                entries.append((entry.name, oid, type_))

    tree = ''.join(f"{type_} {oid} {name} \n" 
                   for name, oid, type_ in sorted(entries))

    return data.hash_object(tree.encode(), 'tree')

'''
we are creating one additional object that collects all the data necessary to store a complete directory 

so lets say in a directory there are two files, so first we will be saving those files first in the object database then the directory in the object database 

so then when we retrieve or use the OID of the directory we techincaly get the directory and the directory content present within the directory.
'''

'''
the below function will take an oid of a tree and then extract it to the working directorywhich is the opposite to the working of the read-tree

'''

def _iter_tree_entries(oid):
    if not oid:
        return 
    tree = data.get_object(oid, 'tree')
    for entry in tree.decode().splitlines():
        pass

'''
the below function is used for ignoring the files that are present inside the .novus_git
directory
'''

def is_ignored(path):
    return ".novus_git" in path.split('/')
