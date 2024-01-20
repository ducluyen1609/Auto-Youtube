import random

def read_txt(file_name):
	return open(file_name, "r", encoding = "utf-8").read()

def save_txt(file_name, write_type, list_content):
	with open(file_name, write_type, encoding = "utf-8") as log:
		log.writelines(content+"\n" for content in list_content)
		log.close()

def int_split(listt):
	temp = []
	for num in listt.split(","): 
		temp.append(int(num))
	return temp

def random_data(file, min = 0):
    rfile = file[random.randint(min, len(file) - 1)]
    return rfile

def cmt_type2(raw_cmt):
	raw_cmt = raw_cmt.replace("(", "\n").replace(")", "\n")
	raw_cmt = raw_cmt.split("\n")

	fi_text = ""
	for cmt in raw_cmt:
		if cmt.find(",") != -1: fi_text += random_data(cmt.split(","))
		else: fi_text += cmt

	return(fi_text)