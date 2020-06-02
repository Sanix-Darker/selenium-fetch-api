FROM python:3.7
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
# Unzip the file
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN mv ./geckodriver ./bin/

CMD bash -C './start.sh';'bash'
