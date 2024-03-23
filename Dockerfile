FROM python:latest

WORKDIR /code_task

COPY requirments.txt /code_task

RUN pip install -U pip
RUN pip install -r requirments.txt

COPY . /code_task

CMD ["python", "wether.py"]