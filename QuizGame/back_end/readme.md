this is back-end
1. activate venv
2. pip install -r requirements.txt
3. 

in folder `config`, create file dbconfig.py where you will store the information of the data:

`
import mysql.connector


connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3300,
    database = "quiz",
    user = "userInDB",  ( my is root)
    password = "password", (mine is ""
    autocommit = True
)
`

To run the server:
    - From our project root folder `Quiz_Project`, type this in terminal: `cd .\back_end\src\`
    - type: `flask run --debug`
