acc = ["tk,mk", "namhocit1,N@mhocit123", "namhocit2,N@mhocit123"]
with open("database/tacc.csv", "w", encoding = "utf-8") as log:
	log.writelines(content+"\n" for content in acc)
	log.close()

a = open("database/acc.csv", "r", encoding = "utf-8").read()
a = [s for s in a.split("\n") if s]
# print(len(a))

# for i in range(10):
# 	for k in range(5):
# 		print(str(i), "aaa")
# 		break
# 		print(k)


while len(a) >= 2:

	print(a.pop(1).split(","))

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		