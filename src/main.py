import os
import shutil
import sys

from copystatic import copy_files_recursive
from website import *

dir_path_static = "./static"
from_path = "content"
template_path = "template.html"
dest_path = "docs"

def main():
    print("Deleting public directory...")
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dest_path)

    default_basepath = "/"
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    else:
        basepath = default_basepath

    generate_pages_recursive(from_path, template_path, dest_path, basepath)

    

main()
