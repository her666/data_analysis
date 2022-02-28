from MySQLdb import _mysql
try:
        db=_mysql.connect("localhost","webuser","raspberry","mysql")
        print('dat shit worked')
except:
        print('database failed to connect')
