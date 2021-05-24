from utils import (
    get_vaccine_availability_data,
    get_email_content_45,
    get_email_content_18,
    is_vaccine_available_45,
    is_vaccine_available_18,
    send_email,
)
from config import (
    VACCINE_AVAILABILITY_DATE,
    DISTRICTS,
    API_URL,
    GET_ALERTS_18,
    GET_ALERTS_45,
    SMTP_HOST,
    EMAIL_FROM,
    EMAIL_TO,
    EMAIL_SUBJECT,
    EMAIL_USER_NAME,
    EMAIL_PASSWORD,
)
import pandas as pd


if __name__ == "__main__":

    try:
        df = get_vaccine_availability_data(
            VACCINE_AVAILABILITY_DATE, DISTRICTS, API_URL
        )
    except:
        df = pd.DataFrame()

    is_available_45 = is_vaccine_available_45(df)
    is_available_18 = is_vaccine_available_18(df)

    if GET_ALERTS_45 and is_available_45:
        html_string_45 = get_email_content_45(df)
    else:
        html_string_45 = ""
    if GET_ALERTS_18 and is_available_18:
        html_string_18 = get_email_content_18(df)
    else:
        html_string_18 = ""
    
    html_to_send = html_string_18 + html_string_45
    
    if (is_available_45 or is_available_18) and html_to_send.strip():
        
        send_email(
            EMAIL_FROM,
            EMAIL_TO,
            EMAIL_SUBJECT,
            html_to_send,
            {"user_name": EMAIL_USER_NAME, "password": EMAIL_PASSWORD},
            SMTP_HOST,
        )
    else:
        print('Vaccine is not available....')
