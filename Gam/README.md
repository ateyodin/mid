# By default the JS page will connect to a sample I've put up at `truck-classifier.heroku.com`.  To have it use your app, just enter the path of your server into the text box with no trailing `/`.  The URL must be fully quaified (i.e. start with `http://` or `https://`)

You can test your code locally before deploying to Heroku by going into the `py` directory and running `python app.py`, you can also just test it on Heroku if you prefer.

If you receive an error from Heroku that says `no web process running` run the following command: `heroku ps:scale web=1`
