pypress
=======

Pypress is a blog plataform develop helping authors to creating collaborative
articles.

How it works
------------

Every time a Entry is saved the system will perfom a commit in a repository
located in the folder specified in the ```ENTRIES_REPO_FOLDER```

How to install
--------------

- Create a virtualenv
```mkvirtualenv pypress```

- Clone repository to development
```git clone git@github.com:raphapassini/pypress.git```

- Clone again in another folder, this folder will work as our entries
```git clone git@github.com:raphapassini/pypress.git pypress_entries```

- The ```pypress``` and ```pypress_entries``` should be in the same level
```
home/
    myuser/
        pypress/
        pypress_entries
```

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

ATTENTION!
-----------
Every time a entry is saved the ```pypress``` will CHECKOUT to ```entries```
branch in order to commit the changes.
If you are developing in the same folder pointed by the ```ENTRIES_REPO_FOLDER```
you'll have HUGE problems.

So, i advise you to follow the steps as described in the How to install section!

