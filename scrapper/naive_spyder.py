def naive_spyder(google_news, news,i):
    article = news[i].copy()
    naive_spyder = google_news.get_full_article(news[i]['url'])
    if naive_spyder:
        article['checks']['naive_spyder'] = True
        naive_article = {
            'authors':naive_spyder.authors,
            'title': naive_spyder.title,
            'text': naive_spyder.text,
            'images': naive_spyder.images
            
        }
        article['naive'] = naive_article
    else:
        article['checks']['naive_spyder'] = False
        article['naive'] = None
    
    return article
    