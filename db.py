import pymysql

class SingletonDB(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instances = super().__call__(*args, **kwargs)
			cls._instances[cls] = instances
		return cls._instances[cls]

class DB(metaclass=SingletonDB):
	def __init__(self,host,name,password,db_name):
		self.connection = pymysql.connect(host=host,user=name,password=password,database=db_name,cursorclass=pymysql.cursors.DictCursor)
	def show_database(self):
		with self.connection.cursor() as cursor:
			cursor.execute("SHOW DATABASES")
			str_res = ""
			while True:
				res = cursor.fetchone()
				if not res:
					break
				else:
					str_res+=f"{res['Database']}\n"
			print(str_res)
		self.connection.close()
