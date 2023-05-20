# Voting Management System Project

## This is my demo project of Voting Management System.

### Requirements :
1. [Python](https://www.python.org/) (supported versions only)
2. [MySQL](https://dev.mysql.com/downloads/)/[MariaDB](https://mariadb.org/) (supported versions only)

### Steps for installing and running the project :
1. In CMD/PowerShell/any Linux Terminal, create virtual environment by following this [link](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/).
2. Enter this command to install Python libraries required to run this project :
```
pip install -r requirements.txt
```
3. Open MySQL/MariaDB. Enter this command :
Windows :
```
SOURCE <path_to_file>\VOTERDB.sql
```
Linux :
```
SOURCE <path_to_file>/VOTERDB.sql
```
4. Exit MySQL/MariaDB.
5. First, enter command to run admin.py :
```
python admin.py
```
Enter `localhost:5000` in web browser.
6. Then, enter command to run voter.py :
```
python voter.py
```
Enter `localhost:5001` in web browser.


> **Note :** Tested in Ubuntu 22.04 and Python 3.10. Dependencies/versions in requirements.txt may subject to change. This project has limitations and other scopes.
