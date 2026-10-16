FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install telethon python-dotenv

CMD ["python3", "main.py"]
