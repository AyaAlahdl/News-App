from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
    newsApi = NewsApiClient(api_key='7cb15d163cd944f38bfd5682e5ad49d9')
    headLines = newsApi.get_top_headlines(sources='techcrunch')
    articles = headLines['articles']
    
    # Lists to store data
    titles = []
    descriptions = []
    images = []
    authors = []
    urls = []
    published_ats = []

    # Extracting data from articles
    for article in articles:
        titles.append(article['title'])
        descriptions.append(article['description'])
        images.append(article['urlToImage'])
        authors.append(article['author'])
        urls.append(article['url'])
        published_ats.append(article['publishedAt'])

    # Zipping data into a single iterable
    news_data = zip(titles, descriptions, images, authors, urls, published_ats)

    return render(request, "main/index.html", context={"news_data": news_data})
