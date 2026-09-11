from data_io import write_account, read_account, write_film, read_film

# Class quản lý tài khoản người dùng
class account_manage():
    # Phương thức init
    def __init__(self):
        self.account_list = read_account()

    # Phương thức đăng nhập
    def login(self, username, password):
        for acc in self.account_list:
            if acc["username"] == username and acc["password"] == password:
                return True # Đăng nhập thành công
        return False # Không tồn tại tài khoản

    # Phương thức đăng ký
    def register(self, username, password):
        for acc in self.account_list:
            if acc["username"] == username:
                print('Da ton tai')
                return False # Đã tồn tại tài khoản
        self.account_list.append({"username": username, "password": password})
        write_account(self.account_list)
        return True # Đăng ký thành công

# Class định nghĩa các đối tượng phim
class film_init():
    def __init__(self, name, date_release, main_actor, director, rating):
        self.name = name                        # Tên phim
        self.date_release = date_release        # Ngày phát hành
        self.main_actor = main_actor            # Diễn viên chính
        self.director = director                # Đạo diễn
        self.rating = rating                    # Điểm đánh giá (thang 10)

# Class quản lý danh sách đối tượng phim
class film_manage:
    def __init__(self):
        self.film_list = list()
        self.film_list_dict = read_film()

    # Phương thức load dữ liệu dict sang dạng danh sách đối tượng
    def load_data(self):
        for film_dict in self.film_list_dict:
            film = film_init(name = film_dict["name"],
                            date_release = film_dict["date_release"],
                            main_actor = film_dict["main_actor"],
                            director = film_dict["director"],
                            rating = film_dict["rating"])
            self.film_list.append(film)

    # Phương thức trả về film bằng cách tìm kiếm qua tên
    def get_film_by_name(self, search_name):
        for film in self.film_list:
            if film.name == search_name:
                return film
        return None

    # Phương thức thêm phim vào danh sách
    def add_film(self, film_dict):
        new_film = film_init(name = film_dict["name"],
                            date_release = film_dict["date_release"],
                            main_actor = film_dict["main_actor"],
                            director = film_dict["director"],
                            rating = film_dict["rating"])
        self.film_list.append(new_film)
        self.film_list_dict.append(film_dict)
        write_film(self.film_list_dict)

    # Phương thức sửa thông tin phim
    def edit_film(self, search_name, new_film):
        # Tìm bộ phim muốn sửa
        matched = self.get_film_by_name(search_name)

        if matched != None:
            matched.name = new_film.get("name", matched.name)
            matched.date_release = new_film.get("date_release", matched.date_release)
            matched.main_actor = new_film.get("main_actor", matched.main_actor)
            matched.director = new_film.get("director", matched.director)
            matched.rating = new_film.get("rating", matched.rating)

        # Ghi dữ liệu vào trong data
        self.film_list_dict = [film.__dict__ for film in self.film_list]
        write_film(self.film_list_dict)

    # Phương thức xóa phim khỏi danh sách
    def delete_film(self, search_name):
        # Tìm bộ phim muốn sửa
        matched = self.get_film_by_name(search_name)

        if matched != None:
            self.film_list.remove(matched)

            # Ghi dữ liệu vào trong data
            self.film_list_dict = [film.__dict__ for film in self.film_list]
            write_film(self.film_list_dict)

    # Phương thức tìm kiếm phim theo tên
    def search_film(self):
        pass

    # Phương thức trả về danh sách tên các bộ phim
    def get_name_list(self):
        name_list = list()
        for film in self.film_list:
            name_list.append(film.name)
        return name_list