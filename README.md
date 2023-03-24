# Db-and-Server-For-Awareness-Detection-App
## Description
This is a server and database system designed to support the Driver Awareness Monitoring app.</br>
The app, which can be accessed through its GitHub repository [here](https://github.com/Ella475/Driver-Awareness-Monitoring), uses a Python-based Flask server to interact with a MySQL database.</br>
The database is created and managed using Python code.

## Installation
1. Download MySQL.
2. Edit the credentials.json file to contain your MySQL username and password.
3. Install the necessary requirements by running the following command in your terminal:
```bash
pip install -r requirements.txt
```
4. Create the database by running the following command in the terminal:
```bash
python -m run_db
```
You can delete the existing database and tables using the -d flag before creating new ones.

5. Run the server by running the following command in the terminal:
```bash
python -m run_server
```
## Usage
The server is utilized by the app to store and retrieve data from the database.</br> 
The server is also responsible for processing the data before and after it is saved in the database.

## License
[MIT](https://choosealicense.com/licenses/mit/)



