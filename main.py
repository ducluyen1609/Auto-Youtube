from time import sleep
import threading
import traceback

from ytb_bot import Ytb_Bot
from ytb_bot_display import Ytb_Bot_Display
from database_driver import *

class Main(Ytb_Bot_Display):
	def __init__(self):
		super().__init__()
		self.acc_bug = []

	def check_input(self):
		try: 
			self.time = float(self.entry_time.get())
			self.cmt = [s for s in self.filecom.split("\n") if s]
			self.link = [s for s in self.filelink.split("\n") if s]
			self.acc = [s for s in self.fileacc.split("\n") if s]
			self.file_acc_dir = self.textacc.get("1.0", "end").strip()
			return True
		except: 
			self.Notify("Lỗi", "Kiểm tra lại đầu vào\n{err}".format(err = traceback.format_exc()))
			return False

	def update_file_acc(self):
		acc = self.acc.pop(0).split(",")
		save_txt(self.file_acc_dir, "w", self.acc)
		return acc

	def update_file_bug(self, acc_bug):
		self.acc_bug.append(acc_bug)
		save_txt("database/bug_log.txt", "w", self.acc_bug)

	def Logic(self):
		try: 
			while len(self.acc) >= 1:
				bot = Ytb_Bot()

				acc = self.update_file_acc()
				bot.login(tk = acc[0], mk = acc[1])

				for link_num in range(len(self.link)):
					bot.driver.get(self.link[link_num])
					if bot.check_not_login(self.link[link_num]): self.update_file_bug(acc[0]); break

					bot.auto_like_sub()
					cmt = random_data(self.cmt)
					if cmt.find("(") != -1: cmt = cmt_type2(cmt)
					bot.auto_cmt(cmt)

					sleep(self.time * 60)

				bot.driver.quit()

			self.Notify("Thông Báo", "Đã chạy xong")

		except: 
			self.Notify("Lỗi Logic", traceback.format_exc())
			return False

	def Start(self):
		if not self.check_input(): return False
		self.screen.title(self.title +" (Running)")

		thread = threading.Thread(target=self.Logic)
		thread.start()

	def Check(self):

		try:
			self.Show_Output("(Cmt:  {cmt})\n\n (Link: {link})\n\n (Acc:  {acc})".format(
				cmt = len(self.cmt), link = len(self.link), acc = len(self.acc)
				)
			)

		except: 
			if self.check_input(): self.Check()





	# def test(self):
	# 	try:
	# 		self.file_acc_dir = self.textacc.get("1.0", "end").strip()
	# 		print(self.file_acc_dir)



main = Main()
main.Interact(func_start = main.Start, func_check = main.Check)