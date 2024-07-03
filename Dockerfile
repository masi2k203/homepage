FROM python:3.12-slim-bullseye as builder

WORKDIR /usr/src/app
ENV FLASK_APP=webapp/__init__.py

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

FROM python:3.12-slim-bullseye as app

ENV TZ Asia/Tokyo
ENV FLASK_APP=webapp/__init__.py

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY ./webapp /usr/src/app/webapp
WORKDIR /usr/src/app

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]