pypress
=======

Pypress is a blog plataform develop helping authors to creating collaborative
articles.

How to install
--------------

- Create a virtualenv
```mkvirtualenv pypress```

- Clone repository to development
```git clone git@github.com:raphapassini/pypress.git```

- Go to ```pypress``` folder
```
cd pypress
```

- Install all requirements
```
pip install -r requirements.txt
```

- Sync database
```
python manage.py syncdb
python manage.py migrate
```
