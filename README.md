# issara_test_job

The first thing to do is to clone the repository:

    $ git clone https://github.com/anandpandayyy/issara_test_job.git
    $ cd KeyValue  

Create a virtual environment to install dependencies in and activate it:

    $ virtualenv2 --no-site-packages env
    $ source env/bin/activate

Then install the dependencies:

(env)$ `pip install -r requirements.txt`

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

    (env)$ cd KeyValue
    (env)$ python manage.py runserver


And navigate to http://127.0.0.1:8000/values

Installing Redis

1. Download the redis-latest.zip native 64bit Windows port of redis
   
    wget https://github.com/ServiceStack/redis-windows/raw/master/downloads/redis-latest.zip

2. Extract redis64-latest.zip in any folder, e.g. in c:\redis

3. Run the redis-server.exe using the local configuration
    
    cd c:\redis
    
    redis-server.exe redis.windows.conf

4. Run redis-cli.exe to connect to your redis instance
    
    cd c:\redis
    
    redis-cli.exe