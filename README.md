# Firestore helper tool

This tools allows to set and get collections from firestore thanks to csv files.

## Installation

### For users

Install the package [from GitHub](https://pip.pypa.io/en/stable/reference/pip_install/#git).

```bash
(venv) C:\Users\Adrien>pip install git+https://github.com/afaucon/firestore_helper.git@v0.0.1
(venv) C:\Users\Adrien>pip list
```

### For developpers

Clone the package from GitHub and install it in editable mode (i.e. [setuptools "develop mode"](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)).

```bash
(venv) C:\Users\Adrien>git clone git+https://github.com/afaucon/firestore_helper.git
(venv) C:\Users\Adrien>pip install --editable firestore_helper
(venv) C:\Users\Adrien>pip list
```

## Usage

Within a python module:

```python
import firestore_helper

firestore_helper.__author__
firestore_helper.__version__
```

```python
import firestore_helper

key = os.environ.get('FIREBASE_ADMIN_KEY')
db = firestore_helper.get_database(key, 'https://my_project.firebaseio.com')
for document_name, content in firestore_helper.get_collection(db, collection_name):
    print("{} => {}".format(document_name, content))
```

With the command line interface:

```bash
(venv) C:\Users\Adrien>python -m firestore_helper get-coll --key secrets/firebase-admin-key.json users https://my_project.firebaseio.com
```

Or directly:

```bash
(venv) C:\Users\Adrien>firehelper get-coll --key secrets/firebase-admin-key.json users https://my_project.firebaseio.com
```
