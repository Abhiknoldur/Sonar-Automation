# Sonar-Automation
SonarScanner.py is a script to automate the process of scanning the project and publish the reports to SonarQube server. This script should be ideally used if your project is not able to use the built in SonarQube plugins for any language.


### Pre-requisites

*Python3*

*pip3*

If you don't have above already then run
```
sudo apt-get update
sudo apt install -y python3
sudo apt-get -y install python3-pip
```

### Steps to run the script
1. Clone this repo using
```
git clone https://github.com/Abhiknoldur/Sonar-Automation.git
```
2. Generate sonar.properties for your project and keep it in the root of the project you are going to scan
```
# must be unique in a given SonarQube instance
sonar.projectKey=my:project

# --- optional properties ---

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0
 
# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.
 
# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```
3. Make sure to run following commands before executing the script
```
pip3 install -r requirements.txt
```
4. Command to run the script:

```
python3 sonarScanner.py
```

5. It will ask the project you want to scan

e.g.

```
Enter the complete path of the project directory
/home/test-user/ProjectDirectory
```
6. It will ask name of the project, you want to set on SonarQube

```
Enter the Name of the project  ................
Test-project
```

After this it'll start the scanning and publish your report to sonarQube.

and We are Done !!! 


Please provide feedback if you see any issues in the solution.

