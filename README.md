# Cowin Automate

Automation script to collect vaccination availability data and send vaccination availability emails by utilizing Cowin API.

## Installation

Clone the [source repository](https://github.com/kartikeyas00/cowin-automate) from Github.
```sh
$ git clone https://github.com/kartikeyas00/cowin-automate.git
```
Install the required python libraries from `requirements.txt` file.
```sh
$ pip install -r requirements.txt 
```

## Usage

Once installed, this is very easy to use. First, change the configurations in the `config.py` file according to your need.

Then setup the sqlite3 database by running the `create_db.py` file:
```sh
$ python create_db.py
```

To get the email updates, run `email_alerts.py` file:
```sh
$ python email_alerts.py
```

To collect the data in the created database, run `data_collector.py` file:
```sh
$ python data_collector.py
```

## Possible Use Cases

There can be multiple use cases for this project:

1. use `email_alerts.py` file to send vaccine availability alerts periodically by automating the script with Crontab or task scheduler in case of windows.
2. use `data_collector.py` file to collect data periodically which can be used for research purposes or buiding a service of some kind.

## Contributing 

If you would like to contribute to this project, please follow these steps:

1. fork this repository
2. make your changes
3. Submit a pull request and describe your changes in detail.

## Acknowledgements

- [Co-WIN Public APIs](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2)