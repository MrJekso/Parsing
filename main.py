import math

class Parsing:
	def __init__(self):
		self.name = "Vadim"
	def get_name(self):
		return self.name
	def set_name(self,new_name):
		self.name = new_name
	def download_page(self):
		pass

class Bot:
	pass

class Main:
	def start(self):
		#OSNOVA LOGICA
		main = Parsing()
		age = 18
		print(f"age: {age}")
		print(f"Name:{main.get_name()}")
		main.set_name("Baron")
		print(f"Name:{main.get_name()}")

Main().start()

