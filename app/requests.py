import json
import urllib.request
from .sources import Sources,Articles


# Getting api key
api_key = None
# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['API-KEY']
    base_url = app.config['API_BASE_URL']


def get_news(category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = 'https://newsapi.org/v2/top-headlines?category={}&apiKey=988fb23113204cfcb2cf79eb7ad99b76'.format(category)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)

    return news_results


def process_articles(news_list):
    """
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news "objects
    """
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = Articles(id, name, title, description, url, urlToImage, publishedAt, content)
            news_results.append(news_object)

    return news_results

def get_sources_news():
    """
    Function that gets the json response to our url request
    """
    get_news_url = 'https://newsapi.org/v2/sources?apiKey=988fb23113204cfcb2cf79eb7ad99b76'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_sources(news_results_list)

    return news_results


def process_sources(news_list):
    """
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news "objects
    """

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get(' url')
        content = news_item.get(' content')

        if name:
            news_object = Sources(id, name,  description, url, content)
            news_results.append(news_object)

    return news_results

def get_articles_news(name):
    """
    Function that gets the json response to our url request
    """
    get_news_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=988fb23113204cfcb2cf79eb7ad99b76'.format(name)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_articles(news_results_list)

    return news_results
