# Db-and-Server-For-Awareness-Detection-App
## Description
This is a server and database system designed to support the Driver Awareness Monitoring app.</br>
The app, which can be accessed through its GitHub repository [here](https://github.com/Ella475/Driver-Awareness-Monitoring), uses a Python-based Flask server to interact with a MySQL database.</br>
The database is created and managed using Python code.

## Installation
1. Download MySQL 
2. Change the username and password in the credentials.json to your username and password in MySQL.
3. Install requirements:
```bash
pip install -r requirements.txt
```
4. Create the database by running the following command in the terminal:
```bash
python -m run_db
```
You can use the flag -d to delete the database and tables before creating new ones.

5. Run the server by running the following command in the terminal:
```bash
python -m run_server
```
## Usage
The server is used by the app to store and retrieve data from the database. 
The server is also used to process the data before and after it is stored in the database.

## License
[MIT](https://choosealicense.com/licenses/mit/)



