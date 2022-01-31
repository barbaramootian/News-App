class Sources:
    """
    News class to define News Objects
    """

    def __init__(self, id, name, description, url,content):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.content = content

class Articles:
    def __init__(self, id, name,title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content