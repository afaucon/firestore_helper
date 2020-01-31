import click
import logging
import os.path
import pprint

import firestore_helper



# --------------------------------------------------------------------------------------------------
@click.group()
@click.option('-v', '--verbose', type=click.IntRange(min=0, max=2), default=0)
def fsync_cli(verbose):
    if verbose == 0:
        logging.basicConfig(level=logging.WARNING)
    if verbose == 1:
        logging.basicConfig(level=logging.INFO)
    if verbose == 2:
        # TODO: In this mode, DEBUG log from imported packages are displayed.
        # Example: DEBUG:git.cmd:Popen(['git', 'clone', ...
        logging.basicConfig(level=logging.DEBUG)


@fsync_cli.command()
@click.option('--key',
              help='Firebase admin key as a json file')
@click.argument('collection_name')
@click.argument('database_url')
def set_coll(database_url, key, collection_name):
    """
    Set a collection from a csv file to firestore.
    """

    # TODO: Remove hardcoding
    #firebase_admin_secret_json_file_path = '../secrets/firebase-admin-key.json'
    #database_url = 'https://borning-challenge-96271.firebaseio.com'

    if key == '':
        key = os.environ.get('FIREBASE_ADMIN_KEY')

    db = firestore_helper.get_database(key, database_url)

    # Starts by deleting all the collection
    firestore_helper.delete_collection(db, collection_name)

    csv_filename = collection_name + '.csv'
    csv_table_reader = firestore_helper.TableReader(csv_filename)
    for item in csv_table_reader.read_item():
        document_name = item.pop('id')
        for key in list(item):
            if item[key] == '':
                del item[key]
        firestore_helper.set_document(db, collection_name, document_name, item)


@fsync_cli.command()
@click.option('--key',
              help='Firebase admin key as a json file')
@click.argument('collection_name')
@click.argument('database_url')
def get_coll(database_url, key, collection_name):
    """
    Get a collection from firestore to a csv file.
    """

    # TODO: Remove hardcoding
    #firebase_admin_secret_json_file_path = '../secrets/firebase-admin-key.json'
    #database_url = 'https://borning-challenge-96271.firebaseio.com'

    if key == '':
        key = os.environ.get('FIREBASE_ADMIN_KEY')

    db = firestore_helper.get_database(key, database_url)

    csv_filename = collection_name + '.csv'
    csv_table_writer = None
        
    table = []
    fieldnames = ['id']
    for document_name, item in firestore_helper.get_collection(db, collection_name):
        for key in item.keys():
            if key not in fieldnames:
                fieldnames.append(key)
        item['id'] = document_name
        table.append(item)

    csv_table_writer = firestore_helper.TableWriter(csv_filename, fieldnames)
    for item in table:
        csv_table_writer.write_item(item)


    
if __name__ == '__main__':
    fsync_cli()