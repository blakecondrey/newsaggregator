from flask import Blueprint, render_template
from datetime import datetime, time
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
    "linkedin": "https://www.linkedin.com/in/blakecondrey/"
}

rights = [
    "rights",
    "knights",
    "spite",
    "fights",
    "bytes",
    "nights",
    "tights",
    "writes",
    "excitement",
    "mites"
]

routes = Blueprint("routes", __name__, static_folder="static", 
                    template_folder="templates")

news_api = NewsApiClient(api_key=API_KEY)

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

@routes.route('/')
def home():
    date_time = datetime.now()
    time_now = date_time.strftime("%m/%d/%Y")
    top_headlines = news_api.get_top_headlines(language = 'en')
    output = grab_headlines(top_headlines)
    return render_template('index.html', context=output, 
                    contact = contact_points, 
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/stonks')
def stonks():
    date_time = datetime.now()
    time_now = date_time.strftime("%m/%d/%Y")
    top_headlines = news_api.get_everything(q = 'stocks', language = 'en',
                    sources = 'bbc-news, google-news, the-wall-street-journal')
    output = grab_headlines(top_headlines)
    return render_template('stonks.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/sports')
def sports():
    date_time = datetime.now()
    time_now = date_time.strftime("%m/%d/%Y")
    top_headlines = news_api.get_everything(q = 'sports', language = 'en',
                    sources = 'google-news, espn')
    output = grab_headlines(top_headlines)
    return render_template('sports.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/florida-man')
def florida_man():
    date_time = datetime.now()
    time_now = date_time.strftime("%m/%d/%Y")
    top_headlines = news_api.get_everything(qintitle = 'florida man',
                    language = 'en',
                    sources = 'fox-news, cnn, google-news')
    output = grab_headlines(top_headlines)
    return render_template('florida-man.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/climate-change')
def climate_change():
    date_time = datetime.now()
    time_now = date_time.strftime("%m/%d/%Y")
    top_headlines = news_api.get_everything(q = 'climate change',
                    language = 'en',
                    sources = 'cnn, bbc-news, the-verge, google-news')
    output = grab_headlines(top_headlines)
    return render_template('climate-change.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)

@routes.route('/covid')
def covid():
    date_time = datetime.now()
    time_now = date_time.strftime("%m/%d/%Y")
    top_headlines = news_api.get_everything(q = 'covid',
                    language = 'en')
    output = grab_headlines(top_headlines)
    return render_template('covid.html', context = output, 
                    contact = contact_points,
                    right = random.choice(rights),
                    time = time_now)
