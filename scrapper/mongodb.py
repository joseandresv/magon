from pymongo import MongoClient

class DatabaseManager:
    def __init__(self, client, database_name, collection_name):
        self.client = MongoClient(client)
        self.database_name = database_name
        self.collection_name = collection_name
        self.db = None
        self.collection = None

    def create_database(self):
        if self.database_name not in self.client.list_database_names():
            self.db = self.client[self.database_name]
            print(f"Created database: {self.database_name}")
        else:
            self.db = self.client[self.database_name]
            print(f"Database {self.database_name} already exists")

    def create_collection(self):
        if self.collection_name not in self.db.list_collection_names():
            self.collection = self.db[self.collection_name]
            print(f"Created collection: {self.collection_name}")
        else:
            self.collection = self.db[self.collection_name]
            print(f"Collection {self.collection_name} already exists")

    def insert_document(self, document):
        if self.collection is None:
            print("Collection is not defined. Please create the collection first.")
            return

        result = self.collection.insert_one(document)
        print(f"Inserted document with ID: {result.inserted_id}")

    def find_document(self, query):
        if self.collection is None:
            print("Collection is not defined. Please create the collection first.")
            return None

        document = self.collection.find_one(query)
        return document

    def update_document(self, query, update):
        if self.collection is None:
            print("Collection is not defined. Please create the collection first.")
            return

        result = self.collection.update_one(query, update)
        print(f"Modified {result.modified_count} document(s)")

    def delete_document(self, query):
        if self.collection is None:
            print("Collection is not defined. Please create the collection first.")
            return

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