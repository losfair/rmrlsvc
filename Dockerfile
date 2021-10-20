FROM python:3.8-slim-buster

WORKDIR /app

RUN apt install libxml2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "gunicorn", "-b", "0.0.0.0:3000", "app:app" ]
