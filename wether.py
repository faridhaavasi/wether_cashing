from .env import Api_Key
import requests
import redis
import json
from celery import Celery
r = redis.Redis(host='localhost', port=6379, db=0)

app = Celery('wether', broker='redis://localhost:6379', backend='redis://localhost:6379')

def get_weather_status(city: str):
    """ Returns the total weather information """

    api_key = Api_Key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    return response.json()
@app.task(bind=True)
def wether_citys(self):
    citys = ['tehran', 'karaj', 'tabriz', 'shiraz']
    
    for i in citys:
        r.set(name=i, value=json.dumps(get_weather_status(i)), ex='60')
        print(get_weather_status(i))
app.conf.beat_schedule = {
    'wether_stasus_cache-every-60-seconds': {
        'task': 'wether.wether_citys',
        'schedule': 60.0,
        
    },
}
app.conf.timezone = 'UTC'         

#wether_citys()        