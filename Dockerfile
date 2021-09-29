FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN py -3 -m pip install discord.py
RUN py -3 -m pip install -U discord.py python-dotenv

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD py -3 -u ./main.py