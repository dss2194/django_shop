FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip 'poetry==1.8.3'
RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY mysite .

#CMD ["gunicorn", "mysite.wsgi:application", "--bind"]