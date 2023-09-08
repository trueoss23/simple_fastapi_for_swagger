FROM python

RUN pip install fastapi uvicorn

WORKDIR ./app

COPY . .

CMD ["uvicorn", "main:app", "--host", "213.18.0.30", "--port", "8081"]
