# Real Time Object Detection 
Real Time Object Detection

## Dependency Management of Python/Flask
1.To create python/Flask dependency management
```
pip freeze > requirements.txt
```
2.To Set up and run project on another system/deployment
```
pip install -r requirements.txt
```

## Flask Migrate
1.Install Flask-Migrate
```
pip install Flask-Migrate
```
2.Initialize Flask-Migrate
```
flask db init
```
3.Generate Migration
```
flask db migrate -m "Description of migration"
```
4.Apply Migration
```
flask db upgrade
```
5.Rollback Migration (Optional)
```
flask db downgrade
```
6.Modify the Database Model
```
flask db migrate -m "Your comment or description"
```
and Update migration
```
flask db upgrade
```

## Install and Start SMTP server in local terminal
```
pip install flask-mail
```
Start SMTP server in local environment
```
python -m smtpd -n -c DebuggingServer localhost:1025
```