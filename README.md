# URL Sorter
### How to use
First download all the necessary files, including an `html` bookmarks file and/or a urls `md` file and put them all in one folder.
```
git clone https://github.com/N-Todorov/URL-Sorter.git
```
The `html` file should be called `bookmarks.html` and the url one - `links.md`

Then download all the dependencies
```
pip install beautifulsoup4 lxml
```

Next run the `get_urls.py` script and choose between bookmarks, urls or both.

And finally run the `sort_urls.py`, choose a browser and start sorting.

### Where is everything stored?
The raw data is stored in a `data.json` file.

And the new bookmarks file is stored in a `sorted.html` file.