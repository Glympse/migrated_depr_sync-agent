FROM ubuntu:14.04

# Install Python Setuptools
RUN apt-get install -y python-setuptools

# Install gcc (to compile 'tornado.speedups')
RUN apt-get install -y gcc

# Install pip
RUN easy_install pip

# Bundle app source
COPY . /src

# Add and install Python modules
RUN pip install -r /src/requirements.txt

# Set default container command
ENTRYPOINT ["python"]

# Run the app
CMD ["/src/app.py"]
