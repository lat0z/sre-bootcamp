FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000
WORKDIR /app
ENV FLASK_APP=/app/api.py
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt
COPY . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=8000"]