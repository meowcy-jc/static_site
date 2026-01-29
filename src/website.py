from textnode import *
from htmlnode import *
from splitnode import *
from block import *
import os


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    level = 0
    for block in blocks:
        if block.startswith("# "):
            edit = block[2:]
            title = edit.strip()
            return title
    raise Exception("Exception")
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template_path")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    dir_name = os.path.dirname(dest_path) 
    if not os.path.exists(dir_name):              
        os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_dir = os.listdir(dir_path_content)
    for dir in list_dir:
        from_path = os.path.join(dir_path_content, dir)
        dest_path = os.path.join(dest_dir_path, dir)
        if os.path.isfile(from_path):
            ext = os.path.splitext(from_path)[1].lower()
            if ext in ['.md']:
                dest_path = os.path.splitext(dest_path)[0] + '.html'
                generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    