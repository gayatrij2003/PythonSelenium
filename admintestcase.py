from POM.adminlog import Login, Admin
from time import sleep
from selenium import webdriver

options=webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options=options)
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
log = Login(driver)
log.send_username("Admin")
sleep(2)
log.send_password("admin123")
sleep(2)
log.click_login_button()
sleep(2)
log.admin_click()
sleep(2)
# actual_url=driver.current_url
# assert expected_url==actual_url,"login unsuccessful"
# print("Login Completed")

log1=Admin(driver)
log1.username("Khushi")
sleep(2)
log1.userrole('ESS')
sleep(2)
log1.Ename("Khushibhendi")
sleep(2)
log1.status('data')
print("admin logged in")

actual_url=driver.current_url
assert expected_url==actual_url,"login unsuccessful"
print("Login Completed")