from sys import argv
from automation import email_alerts, data_collector, create_db


usage = """
Usage:
    Once installed, this is very easy to use. First, change the configurations in the `config.py` file according to your need.

    Then setup the sqlite3 database by running the `create_db.py` file:
    $ python main.py create_db

    To get the email updates, run `email_alerts.py` file:
    $ python main.py email_alerts

    To collect the data in the created database, run `data_collector.py` file:
        $ python main.py data_collector

    """


if len(argv) >= 2:
    if argv[1] == "create_db":
        create_db.run()
    elif argv[1] == "data_collector":
        data_collector.run()
    elif argv[1] == "email_alerts":
        email_alerts.run()
    else:
        print(usage)

else:
    print(usage)
