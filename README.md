A weather caching api system
To run, install celery, redis, requests in your virtual environment
Then enter your thermal and run 'celery -A wether woker -l info -P gevent'
Then play celery beat with celery -A wether beat