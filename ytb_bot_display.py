from display_driver import Display

class Ytb_Bot_Display(Display):
    def __init__(self):
        super().__init__()
        self.title = "Auto Youtube 5.2"

    def Interact(self, func_start = None, func_end = None, func_check = None):
        self.screen.title(self.title)

        # thời gian nghỉ
        self.Create_Label(text = "Thời gian nghỉ (phút):", xy = [65,40])
        self.entry_time = self.Create_Entry(width = 8, xy = [210,40])

        # tìm file comment
        self.textcom = self.Create_TextBox(wh = [40,1], xy = [210,80])
        self.Create_Button(text = "Tìm file Comment", wh = [20,1], xy = [50,80], command = lambda: self.Find_File("com"))

        # tìm file link
        self.textlink = self.Create_TextBox(wh = [40,1], xy = [210,120])
        self.Create_Button(text = "Tìm file Link Youtube", wh = [20,1], xy = [50,120], command = lambda: self.Find_File("link"))

         # tìm file acc
        self.textacc = self.Create_TextBox(wh = [40,1], xy = [210,160])
        self.Create_Button(text = "Tìm file Tài khoản", wh = [20,1], xy = [50,160], command = lambda: self.Find_File("acc"))

        # Start - End - Check
        self.Create_Button(text = "Bắt đầu", wh = [20,1], xy = [500,210], command = func_start)
        self.Create_Button(text = "Kết thúc", wh = [20,1], xy = [340,210], command = self.screen.destroy)
        self.Create_Button(text = "Kiểm tra", wh = [20,1], xy = [180,210], command = func_check)
        self.screen.mainloop()
