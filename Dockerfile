FROM python:3.12

WORKDIR /usr/src/app
ENV FLASK_APP=webapp/__init__.py

COPY ./webapp /usr/src/app/webapp
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "3000"]