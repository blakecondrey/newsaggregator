from flask import Blueprint, render_template
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone
from newsapi import NewsApiClient
from dotenv import load_dotenv
import random
import os

import newsapi
load_dotenv()
API_KEY = os.getenv("API_KEY")

contact_points = {
    "email": "condrey.blake1217@gmail.com",
    "github": "https://github.com/blakecondrey",
    "linkedin": "https://www.linkedin.com/in/blakecondrey/",
    "portfolio": "www.blakecondrey.com"
}

rights = [
    "rights",
    "knights",
    "stalactites",
    "fights",
    "bytes",
    "stalagmites",
    "tights",
    "kites"
]

routes = Blueprint("routes", __name__, static_folder="static", 
                    template_folder="templates")


newsapi = NewsApiClient(api_key=API_KEY)

def grab_headlines(top_headlines):
    articles = top_headlines['articles']
    title = []
    desc = []
    img = []
    url = []
    for i in range(len(articles)):
        generated = articles[i]
        title.append(generated['title'])
        desc.append(generated['description'])
        img.append(generated['urlToImage'])
        url.append(generated['url'])
    output = zip(title, desc, img, url)
    
    return output

    # starting new function for time

def get_time():
    time_format = "%m/%d/%Y"
    date_time = datetime.now(timezone('UTC'))
    now_local = date_time.astimezone(get_localzone())
    time_now = now_local.strftime(time_format)

    return time_now

@routes.route('/')
def home():
    time_now = get_time()
    top_headlines = newsapi.get_top_headlines(language = 'en')
    output = grab_headlines(top_headlines)
    return render_template('index.html', context=output, 
                    contact = contact_points, 
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/stonks')
def stonks():
    time_now = get_time()
    top_headlines = newsapi.get_everything(q = 'stocks', language = 'en',
                    sources = 'bbc-news, google-news, the-wall-street-journal')
    output = grab_headlines(top_headlines)
    return render_template('stonks.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/sports')
def sports():
    time_now = get_time()
    top_headlines = newsapi.get_everything(q = 'sports', language = 'en',
                    sources = 'google-news, espn')
    output = grab_headlines(top_headlines)
    return render_template('sports.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/florida-man')
def florida_man():
    time_now = get_time()
    top_headlines = newsapi.get_everything(qintitle = 'florida man',
                    language = 'en',
                    sources = 'fox-news, cnn, google-news')
    output = grab_headlines(top_headlines)
    return render_template('florida-man.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/climate-change')
def climate_change():
    time_now = get_time()
    top_headlines = newsapi.get_everything(q = 'climate change',
                    language = 'en',
                    sources = 'cnn, bbc-news, the-verge, google-news')
    output = grab_headlines(top_headlines)
    return render_template('climate-change.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/covid')
def covid():
    time_now = get_time()
    top_headlines = newsapi.get_everything(q = 'covid',
                    language = 'en')
    output = grab_headlines(top_headlines)
    return render_template('covid.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)
