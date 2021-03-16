import mysql.connector
from sqlalchemy import create_engine


def connect_to_mysql():
    """
    connection to mysql and create database
    :return: cursor
    """
    from conf.connect import mysql_user, mysql_host, mysql_password, database_name
    mydb = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password)
    cursor = mydb.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS """ + database_name)
    cursor.execute("""USE """ + database_name)
    db_connection = create_engine(
        'mysql+pymysql://{0}:{1}@localhost/{2}'.format(mysql_user, mysql_password, database_name))
    return db_connection


def save_to_mysql(db_connect, df_to_save, df_name):
    """
    save a dataframe in the sql database
    :param db_connect:
    :param df_to_save:
    :param df_name:
    :return:
    """
    df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')
