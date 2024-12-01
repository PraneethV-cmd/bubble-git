import os 
import hashlib 

'''
Git stores all the repository information in a subdir called .git, in order to closely resempble what we are doing, we too create a sub dir for the novus_git where we will be storing the information regarding the new repository when we novus_git init it  
'''

GIT_DIR = '.novus_git' 

def init():
    os.makedirs(GIT_DIR) 
    os.makedirs(f"{GIT_DIR}/objects") 

def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open (f"{GIT_DIR}/objects/{oid}", "wb") as out:
        out.write(data)
    return oid

def get_object(oid):
    with open(f"{GIT_DIR}/objects/{oid}", "rb") as f:
        return f.read()

