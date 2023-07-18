# FROM apache/airflow:2.6.1-python3.8
# COPY requirements.txt /requirements.txt
# RUN pip install --user --upgrade pip
# Copy the entire 'weather' directory into the Docker image
# Install the Python package defined in 'setup.py'
# RUN pip install --no-cache-dir --user -r /requirements.txt


FROM apache/airflow:2.6.1-python3.8

# Copy the entire 'weather' directory into the Docker image
COPY ./weather_project /weather_project

# Install the Python package defined in 'setup.py'
RUN pip install --upgrade --user pip
RUN pip install --no-cache-dir --user /weather_project/dist/weather_project-0.1-py3-none-any.whl


