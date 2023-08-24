FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app/project

CMD ["python", "manage.py", "runserver"]