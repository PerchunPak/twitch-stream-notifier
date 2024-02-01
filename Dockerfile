FROM python:3.12 AS poetry

ENV PATH "/root/.local/bin:${PATH}"
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_IN_PROJECT 1

WORKDIR /root
# see DOK-DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update && \
    apt-get install curl -y --no-install-recommends && \
    curl -sSL https://install.python-poetry.org | python -
COPY poetry.lock pyproject.toml ./
RUN poetry install --only main,docker


FROM python:3.12-slim AS base

ENV PYTHONPATH "/app"

WORKDIR /app

RUN groupadd -g 5000 container && useradd -d /app -m -g container -u 5000 container
COPY --from=poetry /root/.venv ./.venv
COPY src/ src/


FROM python:3.12-slim AS git
# Write version for the Sentry 'release' option
RUN apt-get update && \
    apt-get install git -y --no-install-recommends
COPY .git .git
RUN git rev-parse HEAD > /commit.txt


FROM base AS final

COPY --from=git /commit.txt commit.txt
RUN chown -R 5000:5000 /app
USER container

ENV SENTRY_ENVIRONMENT production

CMD [".venv/bin/dumb-init", ".venv/bin/python", "-m", "src"]
