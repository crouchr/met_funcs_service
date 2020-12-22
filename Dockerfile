FROM python:3.8.5-buster
LABEL author="Richard Crouch"
LABEL description="Meteorological Functions microservice"

# Install Python dependencies
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

EXPOSE 9500

CMD ["python3", "met_funcs_service.py"]
