FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update &&\
    apt-get upgrade --yes

RUN useradd --create-home sergryap
USER sergryap
WORKDIR /home/sergryap

#ENV VIRTUALENV=/home/sergryap/venv
#RUN python3 -m venv $VIRTUALENV
#ENV PATH="VIRTUALENV/bin:$PATH"
ENV PATH=".local/bin:$PATH"

COPY --chown=sergryap pyproject.toml poetry.lock /home/sergryap/
RUN python -m pip install --upgrade pip setuptools
RUN pip3 install poetry
RUN poetry install

COPY --chown=sergryap .env proxys_api.py test_api.py ./

RUN poetry run python3 test_api.py