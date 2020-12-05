FROM python:3.6-alpine

COPY src /bot/src
COPY assets /bot/assets


COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "src/bot.py"]
