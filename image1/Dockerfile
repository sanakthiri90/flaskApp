#app1 : server
FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN chmod -R +x ./*

CMD ["python", "app.py"]

VOLUME /myapp
