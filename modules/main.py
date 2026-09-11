import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import modules, dialog

# Đường dẫn tổng của folder (PTI26)
BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Khai báo đường dẫn con
START_PATH = os.path.join(BASE_PATH, 'Sample', 'ui', 'start.ui')
MAIN_PATH = os.path.join(BASE_PATH, 'Sample', 'ui', 'main.ui')

# Class quản lý giao diện start (login, register)
class start(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(START_PATH, self)
        self.account_manager = modules.account_manage() # Tạo đối tượng quản lý tài khoản

        # Tạo các event liên kết nút bấm
        self.lg_gotoregister_button.clicked.connect(self.gotoregister)
        self.rg_backtologin_button.clicked.connect(self.backtologin)
        self.rg_register_button.clicked.connect(self.handle_register) # event đăng ký
        self.lg_login_button.clicked.connect(self.handle_login) # event đăng nhập

    def handle_login(self):
        # Trích xuất dữ liệu tài khoản, mật khẩu người dùng nhập vào
        username = self.lg_userbox.text()
        password = self.lg_passbox.text()

        # Gọi phương thức đăng nhập
        result = self.account_manager.login(username, password)
        if result == False:
            QMessageBox.warning(self, "Failed", "Đăng nhập thất bại, vui lòng thử lại")
        else:
            QMessageBox.information(self, "Success", "Đăng nhập thành công!")
            mainwindow.show()
            self.close()

    def handle_register(self):
        # Trích xuất dữ liệu tài khoản, mật khẩu người dùng nhập vào
        username = self.rg_userbox.text()
        password = self.rg_passbox.text()

        # Gọi phương thức đăng ký tài khoản
        result = self.account_manager.register(username, password)
        if result == False:
            QMessageBox.warning(self, "Failed", "Đăng ký thất bại, vui lòng thử lại")
        else:
            QMessageBox.information(self, "Success", "Đăng ký thành công, mời bạn đăng nhập")
            self.stackedWidget.setCurrentIndex(0)

    # Phương thức chuyển sang trang đăng ký
    def gotoregister(self):
        self.stackedWidget.setCurrentIndex(1)

    # Phương thức chuyển sang trang đăng nhập
    def backtologin(self):
        self.stackedWidget.setCurrentIndex(0)

# Class quản lý giao diện chính (quản lý các bộ phim)
class main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(MAIN_PATH, self)

        # Tạo đối tượng quản lý danh sách phim từ lớp film_manage
        self.film_manager = modules.film_manage()
        self.film_manager.load_data()

        # Hiển thị danh sách tên các bộ phim đã có trong film.json
        name_list = self.film_manager.get_name_list()
        self.listWidget.addItems(name_list)

        # Event bấm nút
        self.m_add_button.clicked.connect(self.add)
        self.m_edit_button.clicked.connect(self.edit)
        self.m_delete_button.clicked.connect(self.delete)

    # Phương thức tạo dialog thêm phim
    def add(self):
        dialog_add = dialog.Dialog()

        if dialog_add.exec():
            inputs = dialog_add.return_data_add() # Lấy dữ liệu người dùng nhập vào
            self.listWidget.addItem(inputs["name"]) # Thêm phim vào listWidget
            self.film_manager.add_film(inputs) # Thêm dữ liệu vào film.json

    # Phương thức tạo dialog sửa phim
    def edit(self):
        curr = self.listWidget.currentRow() # Lấy dòng đang chọn

        if curr == -1:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn 1 bộ phim trước khi sửa")
            return

        name = self.listWidget.currentItem().text() # Trích xuất text ở dòng đang chọn
        film = self.film_manager.get_film_by_name(name) # Tìm bộ phim (theo tên) trong dữ liệu

        if not film:
            QMessageBox.warning(self, "Warning", f"Không tìm thấy phim nào có tên là {name} trong dữ liệu")
            return

        dialog_edit = dialog.Dialog()
        dialog_edit.stackedWidget.setCurrentIndex(1)
        dialog_edit.show_data_edit(film)
        
        # Nếu bấm OK để xác nhận
        if dialog_edit.exec():
            new_data = dialog_edit.return_data_edit()
            self.film_manager.edit_film(name, new_data)
            self.listWidget.clear()
            self.listWidget.addItems(self.film_manager.get_name_list())

    # Phương thức xóa phim đang chọn
    def delete(self):
        curr = self.listWidget.currentRow() # Lấy dòng đang chọn

        if curr == -1:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn 1 bộ phim trước khi xóa")
            return

        name = self.listWidget.currentItem().text()
        reply = QMessageBox.question(self, "Confirm", f"Bạn có chắc chắn muốn xóa phim {name} hay không?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.listWidget.takeItem(curr) # Xóa dữ liệu dòng đang chọn
            self.film_manager.delete_film(name) # Xóa dữ liệu phim trong data
            QMessageBox.information(self, "Success", f"Bạn đã xóa thành công bộ phim {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    startwindow = start()
    startwindow.show()
    mainwindow = main()
    sys.exit(app.exec())