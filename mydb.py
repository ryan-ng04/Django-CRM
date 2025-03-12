import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'luck123321!',
    port=3307
    )

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE crmdb")
print("created")