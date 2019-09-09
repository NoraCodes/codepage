FROM python:3
RUN pip install -U Flask
RUN pip install psycopg2
WORKDIR /
ADD ./src/ /src/
CMD ["python", "/src/webserver.py"]
