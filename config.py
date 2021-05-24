from datetime import date, timedelta

# Database Settings
DATBASE_URL = "cowin_app.db"

# API Settings
API_URL = "https://cowin.gov.in/api/v2/appointment/sessions/public/calendarByDistrict"
VACCINE_AVAILABILITY_DATE = (date.today() + timedelta(1)).strftime("%d-%m-%Y")
DISTRICTS = {
    "Idukki":306,
    #"Mumbai": 395,
    "Thane": 392,
}

# Toggle Alerts by age
GET_ALERTS_18 = True
GET_ALERTS_45 = True

# Email Settings
SMTP_HOST = "smtp.office365.com"
EMAIL_FROM = "your_username@outlook.com"
EMAIL_TO = ["user_name1@gmail.com, user_name2@gmail.com"]
EMAIL_SUBJECT = "**IMPORTANT** Vaccine Is Available"
EMAIL_USER_NAME = "your_username@outlook.com"
EMAIL_PASSWORD = "your_password"
