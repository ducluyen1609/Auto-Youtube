from bot_driver import auto_bot
from time import sleep

class Ytb_Bot(auto_bot):
    def __init__(self):
        super().__init__()

    def login(self, tk, mk):
        sleep(2)
        self.driver.get("https://accounts.google.com/")
        self.try_send(self.xpath_database["Email_Textbox"], tk)
        self.try_send(self.xpath_database["Password_Textbox"], mk)

    def check_not_login(self, link):
        if self.try_click(self.xpath_database["SignIn"], time = 5, roll = False):
            if self.try_find(self.xpath_database["Email_Textbox"], time = 5): return True
            self.driver.get(link)
            if self.try_find(self.xpath_database["SignIn"], time = 5): return True
        return False

    def auto_like_sub(self):
        like_condition = self.try_get_attri(self.xpath_database["Like_button"], attri = "aria-pressed", find = "false")
        if like_condition: self.try_click(self.xpath_database["Like_button"])

        sub_condition = self.try_get_attri(self.xpath_database["Sub_Box"], attri = "aria-label", find = "Đăng")
        if sub_condition: self.try_click(self.xpath_database["Sub_Box"])

    def auto_cmt(self, cmt = "Good"):
        self.try_send(self.xpath_database["Cmt_Box"], cmt)
        self.try_click(self.xpath_database["Enter_Cmt"])