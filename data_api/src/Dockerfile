# ref: [https://runnable.com/docker/python/dockerize-your-flask-application]

FROM python:3.7-slim

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]