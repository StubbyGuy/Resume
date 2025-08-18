

FROM python:latest

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app

COPY hello_world.py /app/

RUN pip install flask

EXPOSE 5000

CMD ["hello_world.py"]




