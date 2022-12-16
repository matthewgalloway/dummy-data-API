FROM python:3.7.0

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/dummy_data_api/

# Requirements copied over to speed up rebuilds
ADD app/requirements/requirements.txt /opt/dummy_data_api/app/requirements/requirements.txt
ADD app/data_package/requirements/requirements.txt /opt/dummy_data_api/app/data_package/requirements/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /opt/dummy_data_api/app/requirements/requirements.txt
RUN pip install -r /opt/dummy_data_api/app/data_package/requirements/requirements.txt

# Copy over app files
ADD app/ /opt/dummy_data_api/app/
ADD ./requirements.txt /opt/dummy_data_api/
ADD ./run.sh /opt/dummy_data_api/


RUN chmod +x ./run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 5000
CMD ["bash", "./run.sh"]