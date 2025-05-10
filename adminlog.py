from seleniumpagefactory.Pagefactory import PageFactory


class Login(PageFactory):
    def __init__(self,driver):
        self.driver=driver

    locators={"username":("NAME","username"),
              "password":("XPATH","//input[@name='password']"),
              "login_button":("TAG", "button"),
              "Admin":("CLASS_NAME","oxd-main-menu-item-wrapper")}

    def send_username(self, data):
        self.username.send_keys(data)

    def send_password(self, data):
        self.password.send_keys(data)

    def click_login_button(self):
        self.login_button.click()

    def admin_click(self):
        self.Admin.click()

class Admin(PageFactory):
    def __init__(self,driver):
        self.driver=driver

    locators={"adminusername":("XPATH","(//input[@class='oxd-input oxd-input--active'])[2]"),
              "userRole":("XPATH","//i[@class='oxd-icon bi-x oxd-sidepanel-header-close']"),
              "EmployeeName":("XPATH","//input[@placeholder='Type for hints...']"),
              "Status":("XPATH","(//div[@class='oxd-select-text--after'])[1]")
              }
    def username(self,data):
        self.adminusername.send_keys(data)

    def userrole(self,data):
        self.userrole.send_keys(data)

    def Ename(self,data):
        self.Ename.send_keys(data)

    def status(self,data):
        self.status.send_keys(data)