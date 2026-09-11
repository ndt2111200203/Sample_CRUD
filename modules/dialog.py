import os
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QFileDialog

# Đường dẫn tổng của folder (PTI26)
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Khai báo đường dẫn con
UI_PATH = os.path.join(BASE_PATH, 'Sample', 'ui', 'dialog.ui')

# Class xử lý giao diện Dialog
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)

    # Phương thức trả về dữ liệu khi thêm phim
    def return_data_add(self) -> dict:
        return {
            "name": self.add_name.text(),
            "date_release": self.add_date_release.text(),
            "main_actor": self.add_main_actor.text(),
            "director": self.add_director.text(),
            "rating": self.add_rating.text()
        }

    # Phương thức trả về dữ liệu khi sửa phim
    def return_data_edit(self) -> dict:
        return {
            "name": self.edit_name.text(),
            "date_release": self.edit_date_release.text(),
            "main_actor": self.edit_main_actor.text(),
            "director": self.edit_director.text(),
            "rating": self.edit_rating.text()
        }

    # Hiển thị dữ liệu khi sửa phim
    def show_data_edit(self, film):
        self.edit_name.setText(film.name)
        self.edit_date_release.setText(film.date_release)
        self.edit_main_actor.setText(film.main_actor)
        self.edit_director.setText(film.director)
        self.edit_rating.setText(str(film.rating))
        