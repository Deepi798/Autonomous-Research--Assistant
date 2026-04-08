from newspaper import Article

def extract_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text[:2000]
    except Exception as e:
        print("Error extracting:", e)
        return ""