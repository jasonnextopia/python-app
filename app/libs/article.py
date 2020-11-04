import nltk
from newspaper import Article

def download_nltk():
    nltk.download('punkt')

def extract(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    return {
        "title": article.title,
        "text": article.text,
        "top_image": article.top_image,
        "summary": article.summary,
        "link": url
    }