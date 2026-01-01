from pathlib import Path

def get_directorio_raiz():
    return Path(__file__).resolve().parent.parent.parent

def get_directorio_templates():
    return Path(__file__).resolve().parent.parent / "templates"

def get_template_path(template_name = ""):
    return Path(__file__).resolve().parent.parent / "public" / "templates" / template_name

def get_public_path(file_name = ""):
    return Path(__file__).resolve().parent.parent / "public" / file_name