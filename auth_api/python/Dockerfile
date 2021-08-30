FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000
WORKDIR /app
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip3 install --upgrade pip
ENV FLASK_APP=api.py
copy requirements.txt requirements.txt 
run pip3 install -r requirements.txt
copy *.py .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=8000"]