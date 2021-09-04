FROM python:3.8.10

COPY app /app

WORKDIR /app

RUN pip3 install -r requirements.txt


EXPOSE 80

CMD ["uvicorn", "Service:app", "--host=0.0.0.0", "--reload", "--port", "80"]