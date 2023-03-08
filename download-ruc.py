import os
import csv
import zipfile
import requests
import django
from requests.exceptions import HTTPError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruc.settings')
django.setup()

from web.models import Ruc

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'files')
EXTENSION = "zip"


def create_ruc_files_dir():
    if not os.path.exists(FILES_DIR):
        os.makedirs(FILES_DIR)


def download_ruc_files():
    base_url = "https://www.set.gov.py/rest/contents/download/collaboration/sites/PARAGUAY-SET/documents/informes-periodicos/ruc/"
    filename = "ruc"

    for i in range(0, 10):
        file_url = f"{base_url}{filename}{i}.{EXTENSION}"
        try:
            response = requests.get(file_url, stream=True)
            if response.status_code == 200:
                with open(os.path.join(FILES_DIR, f"{filename}{i}.{EXTENSION}"), "wb") as fd:
                    for chunk in response.iter_content(chunk_size=128):
                        fd.write(chunk)
        except HTTPError as http_error:
            print(f"HTTP Error: {http_error}")
        except Exception as error:
            print(f"Error: {error}")


def extract_zip_files():
    for file in os.listdir(FILES_DIR):
        abs_filename = os.path.join(FILES_DIR, file)
        if zipfile.is_zipfile(abs_filename):
            with zipfile.ZipFile(abs_filename) as fe:
                fe.extractall(path=FILES_DIR)


def save_ruc_data():
    for file in os.listdir(FILES_DIR):
        abs_filename = os.path.join(FILES_DIR, file)
        if file.endswith('.txt'):
            with open(abs_filename) as ft:
                reader = csv.reader(ft, delimiter="|", quotechar='"')
                for row in reader:
                    data = {
                        'numero': row[0],
                        'nombre': row[1],
                        'dv': row[2],
                        'numero_anterior': row[3],
                        'estado': row[4]
                    }
                    ruc = Ruc(**data)
                    ruc.save()


if __name__ == '__main__':
    create_ruc_files_dir()
    download_ruc_files()
    extract_zip_files()
    save_ruc_data()
