FROM python:3

WORKDIR /app

COPY . .

RUN py -3 -m pip install -U discord.py==1.7.3 python-dotenv

CMD py -3 -u ./main.py