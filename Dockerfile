FROM python:3.12

COPY . /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
