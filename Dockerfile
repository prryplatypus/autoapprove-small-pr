FROM python:3.12-slim

WORKDIR /action

COPY ./src /action

CMD ["/action/main.py"]
ENTRYPOINT ["python3", "-u"]
