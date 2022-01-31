from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles_news,get_sources_news
from newsapi import NewsApiClient

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    all_sources = get_sources_news()
    title = 'Welcome to Global News'
    return render_template('index.html',title=title,all_sources=all_sources)


@main.route('/news/<name>')
def articles(name):
    # # Init
    # newsapi = NewsApiClient(api_key='988fb23113204cfcb2cf79eb7ad99b76')
    """
    View movie page function that returns the movie details page and its data
    """
    top_headlines = get_articles_news(name)
    return render_template('news.html', top_headlines=top_headlines)

@main.route('/general')
def general():
    # # Init
    # newsapi = NewsApiClient(api_key='988fb23113204cfcb2cf79eb7ad99b76')
    """
    View movie page function that returns the movie details page and its data
    """
    top_headlines = get_news('general')
    return render_template('general.html', top_headlines=top_headlines)

