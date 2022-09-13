FROM python:3.10-alpine
WORKDIR /app

COPY requirements_all.txt requirements_all.txt
RUN pip3 install -r requirements_all.txt

COPY . .

CMD [ "python3", "-m" , "uvicorn", "src.main:app", "--host=0.0.0.0", "--port", "80"]