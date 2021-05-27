# Cowin Automate
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

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

Once installed, this is very easy to use. First, change the configurations in the `config.yml` file according to your need.

Then setup the sqlite3 database by giving `create_db` argument in `main.py` file:
```sh
$ python main.py create_db
```

To get the email updates, give `email_alerts` argument to `main.py` file:
```sh
$ python main.py email_alerts
```

To collect the data in the created database, give `data_collector` argument in `main.py` file:
```sh
$ python main.py data_collector
```

## Possible Use Cases

There can be multiple use cases for this project:

1. use `email_alerts` to send vaccine availability alerts periodically by automating the script with Crontab or task scheduler in case of windows.
2. use `data_collector` to collect data periodically which can be used for research purposes or buiding a service of some kind.

## Contributing 

If you would like to contribute to this project, please follow these steps:

1. fork this repository
2. make your changes
3. Submit a pull request and describe your changes in detail.

## Acknowledgements

- [Co-WIN Public APIs](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2)