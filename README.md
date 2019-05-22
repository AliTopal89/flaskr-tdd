# flaskr-tdd
TDD python tutorial


### deployment FYI

I really did miss Heroku! Deployments at first are never really with just a click of a button, but after a thousand years Heroku's deployments and deployment debugging are still intuitive and great. 

On top of [flask TDD](https://github.com/mjhea0/flaskr-tdd#deployment) I did the following to get flask-TDD to deploy:
  - `gunicorn app:app --preload -b 0.0.0.0:5000` - for better error messaging
  - saw in heroku logs `ModuleNotFoundError: No module named 'flask'` and after a bit of searching I also need to add Flask to my requirements and also saw SQLAlchemeny requirement [from](https://github.com/mjhea0/flaskr-tdd/blob/master/requirements.txt)
  - `pip install Flask==1.0.2` , `pip install Flask-SQLAlchemy==2.3.2` 
  - locally also did `pip freeze > requirements.txt`
  - mainly did `heroku run pip freeze`
  - not sure if it is necessary or not but went back to how the original tutorial was setup so I removed `--preload -b 0.0.0.0:5000`
  - ofcourse don't forget to git add and commit then git push heroku master 
  - `heroku open` and boom got it rolling
