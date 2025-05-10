from time import sleep
from selenium import webdriver

from POM.login_page import Login

# from PageobjectModel.LoginPage import Login

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
log = Login(driver)
log.send_username("Admin")
sleep(2)
log.send_password("admin123")
sleep(2)
log.click_on_login()
sleep(2)
actual_url=driver.current_url
assert expected_url==actual_url,"login unsuccessful"
print("Login successfull")

