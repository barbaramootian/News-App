from flask import render_template
from app import app
from newsapi import NewsApiClient


# Views
def get_news(param):
    pass


@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    Getting_popular_news
    popular_movies = get_news('popular')
    print(popular_news)
    upcoming_news= get_news('upcoming')
    now_showing_news = get_news('now_playing')
    title = 'Home - Welcome to Global News'
    message = 'Hello World!'
    return render_template('index.html', message=message, title=title, popular=popular_news, upcoming=upcoming_news,
                           now_showing=now_showing_news)


@app.route('/news')
def news():
    # Init
    newsapi = NewsApiClient(api_key='988fb23113204cfcb2cf79eb7ad99b76')
    """
    View movie page function that returns the movie details page and its data
    """
    top_headlines = newsapi.get_top_headlines(sources='us')

    all_articles = top_headlines['articles']

    titles = []
    desc = []
    url = []
    urlimage = []
    p_date = []

    """
    using for loop
    """
    for i in range(len(all_articles)):
        main_article = all_articles[i]
        """
        appending the content in lists
        """
    titles.append(main_article['title'])
    desc.append(main_article['description'])
    url.append(main_article['url'])
    urlimage.append(main_article['urlToImage'])
    p_date.append(main_article['"publishedAt'])

    # Zip for finding content directly

    contents = zip(titles, desc, url, urlimage, p_date)

    return render_template('news.html', contents=contents)


@app.route('/contact')
def contact():
    """
    View movie page function that returns the movie details page and its data
    """
    return render_template('contact.html')
