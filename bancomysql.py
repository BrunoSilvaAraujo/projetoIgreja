import mysql.connector


conect = mysql.connector.connect(
    host = '185.27.134.10',
    port = '3306',
    #host = 'http://185.27.134.10/db_structure.php?db=ezyro_25392008_ibnpacurso',
    user = 'ezyro_25392008',
    passwd = 'bruno1986'
)

cursor = conect.cursor()
cursor.execute('SHOW DATABASES')

for x in cursor:
    print(x)