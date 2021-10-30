import os

if (os.name == 'posix'):
	print('------------------Updating System')
	update = 'sudo apt-get update'
	os.system(update)
	
	print('------------------Stop apache2 server----------')
	stopapache2 = 'sudo service apache2 stop'
	os.system(stopapache2)
	
	print('------------------Start postgres service from docker container----------')
	startpgserver = 'sudo docker start 40cb923137a6'
	os.system(startpgserver)
	
	print('------------------Start pgAdmin container 882fc69f7593----------------')
	pgAdmin = 'sudo docker start 882fc69f7593'
	os.system(pgAdmin)