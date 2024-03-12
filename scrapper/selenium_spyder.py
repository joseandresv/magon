import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import re



def get_page_content(url, max_retries=3, delay=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            retries += 1
            time.sleep(delay)
    return None


def extract_article_content_selenium(url,proxy=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')
    if proxy is not None:
        options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Find the article content using common HTML tags and classes
    article_tags = [
        {'name': 'article'},
        {'name': 'div', 'class': 'article-body'},
        {'name': 'div', 'class': 'article-content'},
        {'name': 'div', 'class': 'entry-content'},
        {'name': 'div', 'class': 'post-content'},
        {'name': 'div', 'class': 'story-body'},
        {'name': 'div', 'itemprop': 'articleBody'},
        {'name': 'div', 'id': 'article-body'},
        {'name': 'div', 'class': 'article-text'},
        {'name': 'div', 'class': 'post-text'},
        {'name': 'div', 'class': 'post-body'},
        {'name': 'div', 'class': 'rich-text'},
        {'name': 'div', 'class': 'article-content'},
        {'name': 'section', 'class': 'article-body'},
        {'name': 'section', 'class': 'post-content'},
        {'name': 'section', 'class': 'entry-content'},
    ]

    article_content = ''
    for tag in article_tags:
        try:
            if 'class' in tag:
                article_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, tag['class']))
                )
            elif 'id' in tag:
                article_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, tag['id']))
                )
            elif 'itemprop' in tag:
                article_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[@itemprop='{tag['itemprop']}']"))
                )
            else:
                article_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, tag['name']))
                )
            
            paragraphs = article_element.find_elements(By.TAG_NAME, 'p')
            article_content = '\n'.join([p.text for p in paragraphs])
            
            if article_content:
                break
        except (TimeoutException, StaleElementReferenceException):
            continue

    if not article_content:
        # If the article content is still not found, try to extract paragraphs from the entire page
        try:
            paragraphs = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'p'))
            )
            article_content = '\n'.join([p.text for p in paragraphs])
        except (TimeoutException, StaleElementReferenceException):
            pass

    driver.quit()

    # Remove empty lines and extra whitespace
    article_content = re.sub(r"\n+", "\n", article_content).strip()
    article_content = re.sub(r"\s+", " ", article_content)

    return article_content

def extract_article_content_selenium_js(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Wait for the page to load and JavaScript to render the content
    time.sleep(5)  # Adjust the delay as needed

    # Find the article content using common HTML tags and classes
    article_tags = [
        {'name': 'article'},
        {'name': 'div', 'class': 'article-body'},
        {'name': 'div', 'class': 'article-content'},
        {'name': 'div', 'class': 'entry-content'},
        {'name': 'div', 'class': 'post-content'},
        {'name': 'div', 'class': 'story-body'},
        {'name': 'div', 'itemprop': 'articleBody'},
        {'name': 'div', 'id': 'article-body'},
        {'name': 'div', 'class': 'article-text'},
        {'name': 'div', 'class': 'post-text'},
        {'name': 'div', 'class': 'post-body'},
        {'name': 'div', 'class': 'rich-text'},
        {'name': 'div', 'class': 'article-content'},
        {'name': 'section', 'class': 'article-body'},
        {'name': 'section', 'class': 'post-content'},
        {'name': 'section', 'class': 'entry-content'},
    ]

    article_content = ''
    for tag in article_tags:
        try:
            if 'class' in tag:
                article_element = driver.find_element(By.CLASS_NAME, tag['class'])
            elif 'id' in tag:
                article_element = driver.find_element(By.ID, tag['id'])
            elif 'itemprop' in tag:
                article_element = driver.find_element(By.XPATH, f"//*[@itemprop='{tag['itemprop']}']")
            else:
                article_element = driver.find_element(By.TAG_NAME, tag['name'])
            
            paragraphs = article_element.find_elements(By.TAG_NAME, 'p')
            article_content = '\n'.join([p.text for p in paragraphs])
            
            if article_content:
                break
        except (NoSuchElementException, StaleElementReferenceException):
            continue

    if not article_content:
        # If the article content is still not found, try to extract paragraphs from the entire page
        try:
            paragraphs = driver.find_elements(By.TAG_NAME, 'p')
            article_content = '\n'.join([p.text for p in paragraphs])
        except (NoSuchElementException, StaleElementReferenceException):
            pass

    driver.quit()

    # Remove empty lines and extra whitespace
    article_content = re.sub(r"\n+", "\n", article_content).strip()
    article_content = re.sub(r"\s+", " ", article_content)

    return article_content

def scrape_news_article(article):
    
    url = article['url']
    page_content = get_page_content(url)
    
    if page_content:
        # Try extracting content using the existing function first
        article_content = extract_article_content_selenium(url)
        # If the content is empty, try the new function for JavaScript-rendered content
        if not article_content.strip():
            article_content = extract_article_content_selenium_js(url)
        article['content'] = article_content
    else:
        article['content'] = None
    return article
