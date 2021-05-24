from sqlite3 import Error
from config import DATBASE_URL
from utils import create_connection


SQL_CREATE_DAILY_STATISTICS = """
    CREATE TABLE IF NOT EXISTS daily_statistics (
        id integer PRIMARY KEY,
        district_name text NOT NULL,
        min_age_limit integer NOT NULL,
        vaccine text NOT NULL,
        available_capacity integer NOT NULL,
        timestamp datetime
        );
    """


def create_table(conn, create_table_sql):
    """
    Create table from the create_table_sql statement.

    Parameters
    ----------
    conn : sqlite3.Connection
        Sqlite3 connection object.
    create_table_sql : str
        Create table sql statement.

    Returns
    -------
    None.

    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        conn.rollback()
        print(e)


if __name__ == "__main__":
    conn = create_connection(DATBASE_URL)

    # create table
    if conn is not None:
        # create daily_statistics table
        create_table(conn, SQL_CREATE_DAILY_STATISTICS)

    else:
        print("Error! cannot create the database connection.")
