Flask template for YunoHost
===========================

This is a Flask template for YunoHost.

It will setup a basic Hello World app in `/var/www/<appname>`.

You can then use it to : 

- start developing an app
- or install an existing app by replacing the appropriate files
- or package your flask app using this app template

Technologies
------------

- Python 3
- ~~Postgresql~~ (sqlite, but should be able to choose postgres vs. sqlite at install)
- Gunicorn
- SQLAlchemy

Todo
----

- [ ] Really set app label
- [ ] Handle public/private option
- [ ] Enhance database setting and helpers
- [ ] Document how to launch a dev server
- [ ] ???
- [x] Be able to choose between sqlite and postgres
