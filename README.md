# Flask set-up

1. Create virtual enviroment in folder "venv"
> `$ python -m venv venv`

2. Activate virtual environment
> `$ source venv/bin/activate` or `$ venv\Scripts\activate` (Windows command line)

3. Install the required packeges
> `(venv) $ pip install -r requirements.txt`

4. Set FLASK_APP enviroment variable
> `(venv) $ export FLASK_APP=microapp.py` or `(venv) $ set FLASK_APP=microapp.py` (Windows command line)

5. Run Flask
> `(venv) $ flask run`

# Accessing the app

The app is hosted locally at [http://localhost:5000](http://localhost:5000)
