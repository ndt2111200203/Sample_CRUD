import os
import json

# Đường dẫn tổng của folder (PTI26)
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Khai báo đường dẫn con
ACCOUNT_PATH = os.path.join(BASE_PATH, 'Sample', 'data', 'account.json')
FILM_PATH = os.path.join(BASE_PATH, 'Sample', 'data', 'film.json')

# ĐỌC DỮ LIỆU ACCOUNT
def read_account():
    with open(ACCOUNT_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

# GHI DỮ LIỆU ACCOUNT
def write_account(data):
    with open(ACCOUNT_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# ĐỌC DỮ LIỆU FILM
def read_film():
    with open(FILM_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

# GHI DỮ LIỆU FILM
def write_film(data):
    with open(FILM_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

