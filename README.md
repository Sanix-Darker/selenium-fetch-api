# Selenium-fetch-api

This is a basic Flask Rest-Api for a selenium scrapping !


## Requirements
- python (3.x is recommended)


## How to install

- Create your virtual environment
```
virtualenv -p python3 venv
source venv/bin/activate
```

- You need to install all requirements :
```shell-script
pip install -r requirements.txt
```

- Rename the `example.config.txt` to `config.txt` file and change parameters.

- Install geckodriver :
```shell-script
# For linux users

# cd /home/your-user-name
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
# Unzip the file
tar -xvzf geckodriver*
chmod +x geckodriver
# Add it in the directory specify on your config.txt file as GECKO_PATH

# For other OS's users, please check releases on https://github.com/mozilla/geckodriver/releases
```
Put the geckodriver binary file in the root of this directory

## How to launch

To start the selenium fetch-API, you just have to run :
```
sh ./start.sh
# or just
python -m app.main
```
You can found the HTTP-DOCUMENTATIOn here : [CLICK ME](https://documenter.getpostman.com/view/2696027/SztG46Bv?version=latest)

## How to test
To perform tests for this application, you just have to run :
```
sh ./tests.sh

# The content :
# -----------------
# Copy the config txt file to tests directory
cp ./config.txt ./tests/
pytest

# Then you delete it again
rm -rf ./tests/config.txt
```

## Author

- Sanix-darker
