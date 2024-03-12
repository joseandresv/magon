def naive_spyder(google_news, news,i):
    naive_spyder = google_news.get_full_article(news[i]['url'])
    article = news[i].copy()
    naive_article = {
        'authors':naive_spyder.authors,
        'title': naive_spyder.title,
        'text': naive_spyder.text,
        'images': naive_spyder.images
        
    }
    article['naive'] = naive_article
    
    return article
    