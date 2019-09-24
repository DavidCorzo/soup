FROM python:3-alpine

WORKDIR /soup

RUN mkdr /logs

COPY requirements.txt /soup

RUN pip install -r requirements.txt

COPY main.py /app

# COPY ./soup 

CMD ["python","./main.py"]

ENV DEVELOPER="Marcos Cano, David Corzo"
