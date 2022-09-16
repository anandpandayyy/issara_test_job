FROM python:3.8-slim-buster


# 1. Disable python process buffering
ENV PYTHONUNBUFFERED 1

COPY . /app
# 2. Change working directory to /app/server
WORKDIR /app
# 3. Install MySQL and PostgreSQL dev tools
RUN apt-get update && apt-get install gcc default-libmysqlclient-dev libpq-dev -y

# 4. Copy requirements.txt files to Docker image
COPY requirements.txt ./requirements/
RUN echo $ls 
# 5. Install necessary python packages
RUN pip install --upgrade pip && pip install -r ./requirements/requirements.txt

# 6. Run development server that reloads on code changes
# RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
