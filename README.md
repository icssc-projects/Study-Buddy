# Study-Buddy
A web application that helps UCI students find study partners. 

### requirement
* ``python 3.*``
* `virtualenv` package installed with the above python3

## To create virtual environment
* Under the top level folder, run ```virtualenv venv```
* Activate the virtualenv: `source venv/bin/activate`
* After you see `(venv)` on the side of your terminal, run `pip3 install -r requirements.txt` to install all dependencies.

## For developers:
* When you install a new package, always remember run the `pip3 install` command in the virtual environment
* After there is a new package installed, before you commit, run `pip3 freeze > requirements.txt` under the corresponding directory to update the `requirement.txt` file