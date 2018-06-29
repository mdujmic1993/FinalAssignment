from __future__ import division 		# importing division from Python 3
from decimal import Decimal, getcontext # importing high precision calculations
import MySQLdb 							# importing MySQL DB integration

import socket							# importing the socket module for connecting to an external server
import time 							# importing the module that handles time

import random 							# importing the module that will generate random IDs 

getcontext().prec = 100					# setting the precision of Decimal

n = 1									# the loop counter
m = Decimal(3.00)						# the incrementing value in the equation "pi/4 = 1 - 1/3 + 1/5 -1/7..."
qpi = Decimal(1.00)						# 1/4 of pi
rand = 0								# the random number that will serve as an ID 

target_host = "195.201.32.1"			# IP of my test server
target_port = 9999						# the port my server is listening on

try:									# trying to connect to the DB
	db = MySQLdb.connect(host="localhost",	# connecting to the MySQL DB
		user="testuser",
		passwd="testpass",
		db="testdb",
		port=3306)
except:
	print ("Couldn't connect to MySQL, please check if it's running")	# error code

cursor = db.cursor()					# the DB cursor that's used for executing SQL queries

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# creating a socket object to connect to the server
client.connect((target_host, target_port)) 					# specifying where should the socket object connect  

currenttime = str(time.ctime()) 		# grabbing the current time/start of execution of the script
rand = random.randint(9999,99999) 		# generating the ID 
client.send("ID:%s Start of script execution: %s \r\n" % (rand, currenttime))	# sending the data to the remote server

response = client.recv(4096) 			# receiving data from the server

print response							# printing the received data

while (n <= 100000):					# just a while loop
	if (n % 2 == 0):					# if statement that's checking whether the next expression has to be added or subtracted
		qpi = qpi + (Decimal(1.00) / m)	# addition case
	else:
		qpi = qpi - (Decimal(1.00) / m)	# subtraction case
	n += 1								# increasing the counter
	m += 2								# narrowing the approximation 

	cursor.execute("INSERT INTO testdb.testtable VALUES (%s)" % qpi)	# executing the MySQL query
	db.commit()							# committing the changes, saving the changes in the DB

	print qpi							# verbose output

client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# creating a second socket object to connect to the server
client2.connect((target_host, target_port)) 				# specifying where should the socket object connect  

currenttime = str(time.ctime()) 		# grabbing the current time/end of execution of the script
client2.send("ID:%s End of script execution: %s \r\n\r\n" % (rand, currenttime))	# sending the data to the remote server

response = client2.recv(4096) 			# receiving data from the server

print response							# printing the received data