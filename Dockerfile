FROM python:3.5-buster
RUN apt-get update
RUN apt-get install -y libsasl2-dev libldap2-dev nginx supervisor apt-transport-https vim

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set log placeholder
#RUN mkdir -p /usr/src/app/log
#RUN touch /usr/src/app/log/development.log

# add requirements
#ADD ./requirements.txt /usr/src/app/requirements.txt

# add app
ADD . /usr/src/app
WORKDIR /usr/src/app

# install requirements
RUN pip install -r requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY nginx-site.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx-site.conf /etc/nginx/sites-enabled/nginx-site.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start processes
CMD ["/usr/bin/supervisord"]

