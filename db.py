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

	def update_db(self,data):
		with self.connection.cursor() as cursor:
			cursor.execute("INSERT INTO Well (currency, price, otkr, max, min, edit_price, edit_proc) VALUES ('EUR/USD','1,006','0,9902','1,0011','0,9876','+0,0104','23:29:11')")
			self.connection.commit()
			self.connection.close()

	def create_db(self):
		with self.connection.cursor() as cursor:
			cursor.execute("create table Well(id INT NOT NULL AUTO_INCREMENT, currency VARCHAR(100), price VARCHAR(100), otkr VARCHAR(100), max VARCHAR(100), min VARCHAR(100), edit_price VARCHAR(100), edit_proc VARCHAR(100), PRIMARY KEY (id))")
			self.connection.commit()
			self.connection.close()
