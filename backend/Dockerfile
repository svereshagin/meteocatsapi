FROM python:3.12

ENV POETRY_VERSION=1.8.4 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="/project/code"



WORKDIR /project/code

COPY backend/poetry.lock backend/pyproject.toml /project/code/

RUN python -m pip install --upgrade pip

COPY . /project/code
COPY backend/requirements.txt /project/code
RUN pip install -r requirements.txt
