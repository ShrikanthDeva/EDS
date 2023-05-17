import mysql.connector

def connectServer(host, user, password, database=None):
    """
    Connects to a MySQL server.
    
    Args:
        host (str): The host of the MySQL server.
        user (str): The username for the MySQL server.
        password (str): The password for the MySQL server.
        database (str, optional): The name of the database to connect to. Defaults to None.
    
    Returns:
        mysql.connector.connection.MySQLConnection: The connection object for the MySQL server.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if database:
            print(f"Connected to  MySQL server successfully with the {database} database")
        else:
            print("Connected to MySQL server successfully.")
        return connection
    except mysql.connector.Error as error:
        print(f"Failed to connect to server: {error}")


def createDatabase(connection, database):
    """
    Creates a new database on the MySQL server and connects to it.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object for the MySQL server.
        database (str): The name of the database to create.
    
    Returns:
        mysql.connector.connection.MySQLConnection: The connection object for the created database.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {database}")
        cursor.close()
        
        database_connection = connectServer(
            host=connection.host,
            user=connection.user,
            password=connection.password,
            database=database
        )
        
        print(f"Database '{database}' created successfully.")
        return database_connection
    except mysql.connector.Error as error:
        print(f"Failed to create database: {error}")


def getData(connection, query):
    """
    Retrieves data from the MySQL database using a specified query.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object for the MySQL database.
        query (str): The SQL query to execute.
    
    Returns:
        list: A list of tuples containing the retrieved data.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        
        print("Data retrieved successfully:")
        for row in data:
            print(row)
        
        return data
    except mysql.connector.Error as error:
        print(f"Failed to execute query: {error}")

def putData(connection, query):
    """
    Inserts or updates data in the MySQL database using a specified query.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object for the MySQL database.
        query (str): The SQL query to execute.
    
    Returns:
        None
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print("Data inserted/updated successfully.")
    except mysql.connector.Error as error:
        print(f"Failed to execute query: {error}")

def execQuery(connection, query):
    """
    Executes a query on the MySQL database and prints the server's response.
    
    Args:
        connection (mysql.connector.connection.MySQLConnection): The connection object for the MySQL database.
        query (str): The SQL query to execute.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        
        if cursor.with_rows:
            result = cursor.fetchall()
            print("Query executed successfully. Result:")
            for row in result:
                print(row)
        else:
            print("Query executed successfully.")
        
        cursor.close()
    except mysql.connector.Error as error:
        print(f"Failed to execute query: {error}")


# OUERY & RESULTS TESTED

#con = connectServer('localhost','root','shrikanth')
    # -> Connected to MySQL server successfully.

# con = connectServer('localhost','root','shrikanth','firstdb')
    # -> Connected to  MySQL server successfully with the firstdb database

#execQuery(con,"create table user(user_id int);")
    # -> Query executed successfully.

#getData(con,"show tables")
    # -> Data retrieved successfully:
    # -> ('entries',)
    # -> ('user',)

#putData(con,"Insert into user values(1);")
    # -> Data inserted/updated successfully.

# execQuery(con,"select * from user;")
    # -> Query executed successfully. Result:
    # -> (1,)
