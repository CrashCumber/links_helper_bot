FROM python:3.6

COPY ./config.py /
COPY ./bot.py /
COPY ./requirements.txt /
COPY ./models.py /
COPY ./database.py /
COPY ./wait-for-it.sh /

RUN pip install -r /requirements.txt

RUN chmod +x bot.py
RUN chmod 777 wait-for-it.sh

