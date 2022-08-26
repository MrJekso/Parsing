import math
from db import DB

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
		data_base = DB('localhost','test','123','test')
		data_base.show_database()
class Bot:
	pass

class Main:
	def start(self):
		#OSNOVA LOGICA
		obj = Parsing()
		obj.download_data_db([123,123])
Main().start()

