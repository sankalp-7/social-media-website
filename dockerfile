FROM python:3.10
ENV PYTHONUNBUFFERED=1

RUN pip3 install mysqlclient


WORKDIR /djinsta

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt




COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
