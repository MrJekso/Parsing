import math

class Parsing:
	def __init__(self):
		self.login = ""
		self.passwd = ""
		self.server = ""
	#VADIM
	def download_page(self):
		pass
	#VADIM
	def parsing_page(self):
		pass
	def download_data_db(self,data):
		for i in data:
			print(f"KURS: {i}")
class Bot:
	pass

class Main:
	def start(self):
		#OSNOVA LOGICA
		obj = Parsing()
		obj.download_datat_db(["USD 231","EVRO 433","RUB 42"])
Main().start()

