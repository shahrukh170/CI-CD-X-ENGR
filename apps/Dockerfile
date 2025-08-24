# syntax=docker/dockerfile:1.7
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN adduser --disabled-password --gecos "" appuser


FROM base AS deps
CMD MKDIR app/service-a
WORKDIR app/
#COPY app/service-a/ app/service-a/
COPY apps/pyproject.toml app/
COPY apps/requirements.txt app/ 
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install -U pip-tools
CMD /usr/local/bin/pip install -r app/requirements.txt app/pyproject.toml
#RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base AS runtime
COPY --from=deps /usr/local /usr/local
USER root
EXPOSE 8000
COPY src/ app/
COPY src/templates/* templates/
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -m src.healthcheck || exit 1
CMD ["python", "app/main.py"]
