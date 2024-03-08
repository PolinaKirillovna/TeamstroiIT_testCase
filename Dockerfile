FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./api /app/api
COPY ./parser /app/parser
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
