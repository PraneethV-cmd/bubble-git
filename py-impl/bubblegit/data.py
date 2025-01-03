import os 
import hashlib

GIT_DIR = '.bubblegit'

def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')

def set_HEAD(oid):
    with open(f"{GIT_DIR}/HEAD", "w") as f:
        f.write(oid)

def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data 
    oid = hashlib.sha1(obj).hexdigest()
    with open(f"{GIT_DIR}/objects/{oid}", "wb") as out:
        out.write(obj)
    return oid

def get_object(oid, expected='blob'):
    with open(f"{GIT_DIR}/objects/{oid}", "rb") as f:
        obj = f.read()
    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected , f"Expected {expected}, got {type_}"
    return content
