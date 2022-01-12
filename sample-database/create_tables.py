from dotenv import load_dotenv, find_dotenv
from mysql.connector import connect, Error
from os import environ as env, name

from mysql.connector.connection import MySQLConnection

import logging as log

# set up logger
log.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S', 
                    level=log.INFO,
                    handlers=[log.StreamHandler()])

def load_environmental_variables() -> None:
    log.info('Loading environmental variables')

    ENV_FILE = find_dotenv()

    if ENV_FILE:
        load_dotenv(ENV_FILE)
        log.info('Environmental variables loaded successfully.')
    else:
        log.warning('No .env file found. Export failed.')

def connect_to_database() -> MySQLConnection:
    log.info('Connectinig to databse')

    database_host = env.get('DATABASE_HOST')
    database_root_user = 'root'
    database_root_password = env.get('MYSQL_ROOT_PASSWORD')
    database_port = env.get('DATABASE_PORT')

    try:
        connection = connect(host=database_host, user=database_root_user, password=database_root_password, port=database_port)
        log.info('Connected to database successfully.')
        return connection
    except Exception as ex:
        log.warning('Failed to connect to database')
        log.warning(ex)
        return None


def create_database(connection: MySQLConnection) -> None:
    log.info('Creating database and tables')

    cursor = connection.cursor()

    try:
        # create and use database
        database_name = 'user_db'
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name};')
        cursor.execute(f'USE {database_name};')

        # create tables
        USER_TABLE = 'users'
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {USER_TABLE} (user_id VARCHAR(36) PRIMARY KEY, user_name VARCHAR(128));')
        log.info(f'Successfully created {USER_TABLE} table.')

    except Exception as ex:
        log.warning('Failed to create database')
        log.warning(ex)
        return None


if __name__ == '__main__':
    load_environmental_variables()
    connection = connect_to_database()

    if connection is not None:
        create_database(connection=connection)