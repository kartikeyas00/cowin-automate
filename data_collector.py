from utils import (
    get_vaccine_availability_data,
    get_data_for_daily_statistics_table,
    insert_data_to_daily_statistics_table,
)
from config import DATBASE_URL, VACCINE_AVAILABILITY_DATE, DISTRICTS, API_URL
from utils import create_connection


if __name__ == "__main__":

    ### Connect to Sqlite
    conn = create_connection(DATBASE_URL)
    if conn is not None:
        df = get_vaccine_availability_data(
            VACCINE_AVAILABILITY_DATE, DISTRICTS, API_URL
        )
        df_daily_statistics_data = get_data_for_daily_statistics_table(df)
        insert_data_to_daily_statistics_table(df_daily_statistics_data, conn)
