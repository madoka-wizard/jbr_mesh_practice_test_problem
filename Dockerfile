FROM python:3.9.2-alpine3.13

ENV DOCKER_CONTAINER=true \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true \
  PIPENV_DOTENV_LOCATION=/.env

RUN apk --no-cache add \
  ffmpeg \
  tini

COPY . .

RUN chmod +x "/entrypoint.sh" "/simple_audio_processor.py" \
  && pip install pipenv \
  && pipenv install --deploy --system --ignore-pipfile

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
