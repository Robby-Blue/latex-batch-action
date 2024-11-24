import os
import sys
import shutil
import subprocess

base_source_path = sys.argv[1]
base_dest_path = "./pdfs"

def process_folder(source_path, dest_path):
    tex_path = get_file_by_extention(".tex", source_path)
    is_project_folder = tex_path is not None

    if is_project_folder:
        print(tex_path)
        process = subprocess.Popen(["pdflatex", "--shell-escape", "-interaction=nonstopmode",
        "-halt-on-error", "-output-directory=.", tex_path],
            cwd=source_path)
        process.wait()
        if process.returncode != 0:
            return
        pdf_path = get_file_by_extention(".pdf", source_path)
        if not pdf_path:
            return
        if dest_path == base_dest_path:
            dest_path = os.path.join(dest_path, "main")
        parent_dest_path = os.path.dirname(dest_path)
        if not os.path.exists(parent_dest_path):
            os.makedirs(parent_dest_path)
        shutil.copy(pdf_path, dest_path+".pdf")
    else:
        for file_name in os.listdir(source_path):
            file = os.path.join(source_path, file_name)
            if not os.path.isdir(file):
                continue
            process_folder(os.path.join(source_path, file_name),
                    os.path.join(dest_path, file_name))

def get_file_by_extention(extention, path):
    files = os.listdir(path)
    for file in files:
        if file.endswith(extention):
            return os.path.join(path, file)
    return None

process_folder(base_source_path, base_dest_path)