import os 
import argparse
from . import data 

'''
The argparse library will help us to parse the arguments and then will help us to implement some sub commands 
'''
def main():
    args = parse_args()
    args.func(args) 

def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    commands.required = True 

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init) 

    '''
    the flow of the command hash-object is that we get the path of the file to sore
    we read the file
    hash the content of the file using sha-1
    and then store the file under the .novus_git/objects/the hashed value


    we are using content=addresable storage instead of the name-addressable storage.
    github employs more complex version of the content-adresseable method 
    '''

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    return parser.parse_args() 

def init(args):
    data.init() 
    print(f'Created an empty novus_git repository in {os.getcwd()}/{data.GIT_DIR}')

def hash_object(args):
    with open (args.file, 'rb') as f:
        print(data.hash_object(f.read()))
