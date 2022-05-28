from src.extract_data import ExtractSharePointFile
import os
from dotenv import load_dotenv

load_dotenv()

site = os.getenv('site')
username = os.getenv('user')
password = os.getenv('password')
file_name = os.getenv('filename')

print(site, username, password, file_name)

if __name__ == '__main__':
    try:
        sp = ExtractSharePointFile(site, username, password)
        sp.connect().download_file(file_name)
    except Exception as e:
        print(f'ERROR: {e}')
