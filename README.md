# Db-and-Server-For-Awareness-Detection-App
## Description
This is the server and database for the Driver Awareness Monitoring app. The app can be found [here](https://github.com/Ella475/Driver-Awareness-Monitoring)

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



