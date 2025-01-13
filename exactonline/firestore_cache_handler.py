from google.cloud import firestore

class FirestoreCacheHandler:
    """
    FirestoreCacheHandler uses Google Cloud Firestore to cache data.

    Make sure you have authenticated your application with Google Cloud by setting up the appropriate credentials.
    You can do this by setting the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your service account key file:

    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"

    This will allow your code to use Google Cloud Firestore as a cache, enabling it to run in multiple Google Cloud Functions.
    """

    def __init__(self, collection_name='python-exact-online-cache'):
        self.db = firestore.Client()
        self.collection_name = collection_name

    def resetCache(self):
        """
        Resets the cache by deleting all documents in the Firestore collection.
        """
        docs = self.db.collection(self.collection_name).stream()
        for doc in docs:
            doc.reference.delete()
        return {}

    def getCache(self, key):
        """
        Retrieves a cached value from Firestore by key.

        Args:
            key (str): The key of the cached value.

        Returns:
            dict or None: The cached value if it exists, otherwise None.
        """
        doc_ref = self.db.collection(self.collection_name).document(key)
        doc = doc_ref.get()
        if doc.exists:
            value = doc.to_dict()
            return value
        return None
    
    def setCache(self, key, value):
        """
        Sets a value in the Firestore cache.

        Args:
            key (str): The key of the value to cache.
            value (dict): The value to cache.

        Returns:
            dict: The cached value.
        """
        doc_ref = self.db.collection(self.collection_name).document(key)
        doc_ref.set(value)
        return value

    def deleteCache(self, key):
        """
        Deletes a cached value from Firestore by key.

        Args:
            key (str): The key of the cached value to delete.
        """
        doc_ref = self.db.collection(self.collection_name).document(key)
        doc_ref.delete()