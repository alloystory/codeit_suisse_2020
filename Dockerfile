FROM python:3.7
WORKDIR /usr/app

COPY src /usr/app/src
COPY requirements.txt /usr/app
COPY run.sh /usr/app

RUN pip install -r requirements.txt
RUN chmod +x run.sh
ENTRYPOINT [ "./run.sh", "prod" ]