from django.shortcuts import render

from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsApi = NewsApiClient(api_key = '7cb15d163cd944f38bfd5682e5ad49d9')
    headLines = newsApi.get_top_headlines(sources = 'techcrunch')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    myist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": myist})