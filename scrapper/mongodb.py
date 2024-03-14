from pymongo import MongoClient

class DatabaseManager:
    def __init__(self, database_name, collection_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database_name = database_name
        self.collection_name = collection_name
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]

    def insert_document(self, document):
        result = self.collection.insert_one(document)
        print(f"Inserted document with ID: {result.inserted_id}")

    def find_document(self, query):
        document = self.collection.find_one(query)
        return document

    def update_document(self, query, update):
        result = self.collection.update_one(query, update)
        print(f"Modified {result.modified_count} document(s)")

    def delete_document(self, query):
        result = self.collection.delete_one(query)
        print(f"Deleted {result.deleted_count} document(s)")

    def create_document(self, title, description, published_date, url, publisher_href, publisher_title,
                        naive_spyder, selenium_spyder, authors, naive_title, naive_text, images, content):
        document = {
            'title': title,
            'description': description,
            'published_date': published_date,
            'url': url,
            'publisher': {
                'href': publisher_href,
                'title': publisher_title
            },
            'checks': {
                'naive_spyder': naive_spyder,
                'selenium_spyder': selenium_spyder
            },
            'naive': {
                'authors': authors,
                'title': naive_title,
                'text': naive_text,
                'images': images
            },
            'content': content
        }
        return document