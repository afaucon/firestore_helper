# https://firebase.google.com/docs/admin/setup/

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

def get_database(firebase_admin_secret_json_file_path, databaseURL):
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(firebase_admin_secret_json_file_path)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': databaseURL
    })

    db = firestore.client()

    return db

def set_document(db, collection_name, document_name, content):
    db.collection(collection_name).document(document_name).set(content)

def get_collection(db, collection_name):
    collection_ref = db.collection(collection_name)
    documents = collection_ref.stream()

    for doc in documents:
        document_name = doc.id
        content = doc.to_dict()
        yield document_name, content

def delete_collection(db, collection_name, batch_size=20):
    collection_ref = db.collection(collection_name)

    def delete_batch_recurse(collection_ref, batch_size):
        docs = collection_ref.limit(batch_size).stream()
        deleted = 0

        for doc in docs:
            print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return delete_batch_recurse(collection_ref, batch_size)

    delete_batch_recurse(collection_ref, batch_size)