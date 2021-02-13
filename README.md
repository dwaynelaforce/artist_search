
# ARTIST SEARCH APP

Artist Search App is a simple app for searching for artists on a list.

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

## Usage

The list of artist names is stored in artist_search_app/static/artist_list.txt.  When submitting a search request the app will search line by line through that file for matches.  That file can be edited to include different data, but changing the file name will break the app.  Each artist name should be without quotes and separated by a new line.  Any other special characters used as separators (such as commas) will be interpreted as part of the artist name.

Most of the code is written in artist_search_app/views.py and that file has detailed comments.

## Future plans/features:

If there is demand, the following features can be implemented:

1. Refactoring the code to work with Django's included sqlite database instead of a static text file.
2. Creating an admin page for addition/deletion of artists from the database.
3. Adding other models/relationships to database such as music albums attributed to the artist.







