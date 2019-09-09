FROM python:3
RUN pip install -U Flask
WORKDIR /
ADD ./src/ /src/
CMD ["python", "/src/webserver.py"]
