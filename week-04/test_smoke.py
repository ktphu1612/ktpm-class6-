from selenium import webdriver


def test_open_the_internet():
    # 1. Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # 2. Mở trang web the-internet
        driver.get("https://the-internet.herokuapp.com/")

        # 3. Kiểm tra xem tiêu đề trang (title) có đúng là "The Internet" không
        assert driver.title == "The Internet"

    finally:
        # 4. Đóng trình duyệt sau khi kiểm tra xong
        driver.quit()