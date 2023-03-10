FROM python:3.11

WORKDIR /python-project

COPY ./requirements.txt /python-project/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /python-project/requirements.txt

COPY ./main.py /python-project/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]