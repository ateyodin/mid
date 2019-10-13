You can test your code locally before deploying to Heroku by going into the `py` directory and running `python app.py`, you can also just test it on Heroku if you prefer.

If you receive an error from Heroku that says `no web process running` run the following command: `heroku ps:scale web=1`
