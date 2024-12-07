import os 
import sys 
import argparse
from . import data 
from . import base

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

    '''
    there is a command in git namely 'cat-file' which does the opposite compared to 
    hash-object, where we print the file that is attirbuted to the hash 
    for eg if the file is say sample.txt and the hash of it is asd123 
    with hash-object we get the asd123 value but with the cat-file we get the name of the file that is attributed to the hash which is sample.txt
    '''

    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    write_tree_parser = commands.add_parser('write-tree')
    write_tree_parser.set_defaults(func=write_tree)
    write_tree_parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help="Directory to write as a tree (default: current directory)"
    )

    return parser.parse_args() 

def init(args):
    data.init() 
    print(f'Created an empty novus_git repository in {os.getcwd()}/{data.GIT_DIR}')

def hash_object(args):
    with open (args.file, 'rb') as f:
        print(data.hash_object(f.read()))


def cat_file(args):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object, expected=None))


def write_tree(args):
    print(base.write_tree())

