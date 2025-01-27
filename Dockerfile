FROM python:3.12.6-alpine3.20

ENV PYTHONUNBUFFERED=1

RUN apk update && \
    apk add --no-cache gcc musl-dev mariadb-dev python3-dev libffi-dev pkgconfig

WORKDIR /BackendProjecto

COPY ./requirements.txt  ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]