
# ARTIST SEARCH APP

Artist Search App is a simple app for searching for artists.

## Installation

### Requirements

This project was coded in a Python 3.9.1 environment.  Earlier versions of Python 3 will likely work but this has not been tested.  You can download Python here: https://www.python.org/downloads/

### How to install and run

Git: Clone and download this repository by running the following command in a bash terminal in a directory of your choosing:

```bash
git clone https://github.com/dwaynelaforce/artist_search.git
```

Alternatively you can download the zip file and unpack it in the chosen directory.

Navigate into artist_search folder in your terminal (it might be named artist_search-master depending on how it was downloaded):

```bash
cd artist_search/
```

Before moving on to the next step it is recommended that you start a virtual environment, though it is not strictly required.  For more information on virtual environments please see the Python documentation at https://docs.python.org/3/tutorial/venv.html.

Run the following command to install required packages:

```bash
pip install -r requirements.txt
# mac users, if that doesn't work try this:
pip3 install -r requirements.txt
```

Run the program:

```bash
python manage.py runserver
# mac users, if that doesn't work try this:
python3 manage.py runserver
```

In a web browser of your choosing, navigate to http://localhost:8000.







