import os
import yaml
from datetime import date, timedelta

with open(os.path.dirname(__file__) + "/../config.yml") as f:
    config = yaml.safe_load(f)

    if config["VACCINE_AVAILABILITY_DATE"]:
        VACCINE_AVAILABILITY_DATE = config["VACCINE_AVAILABILITY_DATE"]
    else:
        VACCINE_AVAILABILITY_DATE = (date.today() + timedelta(1)).strftime("%d-%m-%Y")

    DATBASE_URL = config["DATBASE_URL"]
    DISTRICTS = config["DISTRICTS"]
    API_URL = config["API_URL"]
    GET_ALERTS_18 = config["GET_ALERTS_18"]
    GET_ALERTS_45 = config["GET_ALERTS_45"]
    SMTP_HOST = config["SMTP_HOST"]
    EMAIL_SUBJECT = config["EMAIL_SUBJECT"]
    EMAIL_PASSWORD = config["EMAIL_PASSWORD"]
    EMAIL_TO = config["EMAIL_TO"]
    EMAIL_USER_NAME = config["EMAIL_USER_NAME"]
    EMAIL_FROM = config["EMAIL_FROM"]
