#Program to run SonarQube, SonarScanner and ElasticSearch which will scan a repo and provide results.

import sys
from threading import Thread
import os
import zipfile
import subprocess
import time
import urllib.request
import urllib
import datetime
import requests
from subprocess import Popen
import platform
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from shutil import unpack_archive
import shutil


# Get the current directory where the script is running
dir_path = os.path.dirname(os.path.realpath(__file__))


# ************************************************************************************
# Function to download Sonar-scanner
# ************************************************************************************
def downloadSonarScanner():
	print("Downloading Sonar-scanner ... \n")
	zipurl = 'https://github.com/Abhiknoldur/Sonar-Automation/raw/main/sonar-scanner.zip'
	with urlopen(zipurl) as zipresp, NamedTemporaryFile() as tfile:
		tfile.write(zipresp.read())
		tfile.seek(0)
		unpack_archive(tfile.name, './sonar-scanner/', format = 'zip')


# ************************************************************************************
# Function to copy the project code to sonar-scanner
# ************************************************************************************



def copyProject(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
# ******************************************************************************************************************
# Function to download the repository taken as an arguement
# ******************************************************************************************************************

def setupProject():

	# Snippet to find the filename from the URL
	
	# [url_first_part,mname]=url.rsplit('/', 1)
	prjDirectory = input("Enter the complete path of the project directory  ................ \n")
	mname = input("Enter the Name of the project  ................ \n")

	subprocess.call("mkdir -p sonarScanner/bin/project",shell=True)
	# Path where you want to download the project
	dest = dir_path+'/sonarScanner/bin/project/'+mname
	if not os.path.exists(dest):
		os.mkdir(dest)
	print("\nProject setup Started ............ \n")
	# Cloning the repo into the path1 variable
	copyProject(prjDirectory, dest)

	print("\nThe repo has been copied in our system .................... \n")

	# Path of the properties file
	propertiesFilePath = dir_path + '/sonar-scanner/sonar-scanner/sonar-scanner-4.5.0.2216-linux/conf/sonar-scanner.properties'

	# Reading the properties File and deleting all the contents in them

	print("\nDeleting Old properties ................ \n")

	f = open(propertiesFilePath, 'r+')
	f.truncate(0)
	data = f.readlines()

	#  Appending the properties in the file one by one
	data.append("sonar.sourceEncoding=UTF-8")
	data.append("\n")
	data.append("\n")
	data.append("export SONAR_SCANNER_OPTS=-Xms512m\ -Xmx2048m")
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectKey="+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectName="+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.projectVersion=1.0")
	data.append("\n")
	data.append("\n")
	data.append("sonar.scm.disabled=true")
	data.append("\n")
	data.append("\n")

	#data.append("sonar.nodejs.executable=/usr/local/n/versions/node/11.6.0")

	data.append("sonar.sources="+dir_path+"/sonarScanner/bin/project/"+mname)
	data.append("\n")
	data.append("\n")
	data.append("sonar.java.binaries="+dir_path+"/sonarScanner/bin/project/"+mname)

	# and write everything back
	with open(propertiesFilePath, 'w') as file:
		file.writelines(data)

	# Running the command for scanning the files

	# Changing the mod for sonarScanner in Unix

	print("\nChanging the mode of sonar Scanner cli ............. \n")
	subprocess.call("chmod -R 777 ./sonar-scanner/sonar-scanner/sonar-scanner-4.5.0.2216-linux/bin/sonar-scanner",shell=True)
	subprocess.call("chmod +x /sonar-scanner/sonar-scanner/sonar-scanner-4.5.0.2216-linux/jre/bin/java",shell=True)
	bashCommand = './sonar-scanner/sonar-scanner/sonar-scanner-4.5.0.2216-linux/bin/sonar-scanner'

	print("\nRunning sonarScanner.sh file.\nScanning of " + mname + " repo started ................. \n")
	# Running the sonarScanner in Unix
	process = subprocess.call(bashCommand, shell=True)

	tempTime = str(datetime.datetime.now())
	os.rename(dest,dest+tempTime)


# Function to start the project setup and run sonarScanner in different threads
#***********************************************************************************************************************

if __name__ == '__main__':
	if sys.platform=="linux1" or sys.platform=="linux2" or sys.platform=="linux":
		print("Linux recognised ... \n")
		sonarClidest = dir_path+'/sonar-scanner'
		if not os.path.exists(sonarClidest):
			Thread(target=downloadSonarScanner).start()
			time.sleep(240)
		Thread(target=setupProject).start()
