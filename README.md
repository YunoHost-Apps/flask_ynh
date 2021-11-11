# Flask template for YunoHost

[![Integration level](https://dash.yunohost.org/integration/flask.svg)](https://dash.yunohost.org/appci/app/flask) ![](https://ci-apps.yunohost.org/ci/badges/flask.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/flask.maintain.svg)  
[![Install Flask Template with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=flask)

> *This package allow you to install Custom Webapp quickly and simply on a YunoHost server.  
If you don't have YunoHost, please see [here](https://yunohost.org/install) to know how to install and enjoy it.*

## Overview

This is a Flask template for YunoHost.

It will setup a basic Hello World app in `/var/www/<appname>`.

You can then use it to :

- start developing an app
- or install an existing app by replacing the appropriate files
- or package your flask app using this app template

## Technologies

- Python 3
- Flask
- SQLAlchemy
- PostgreSQL or MySQL (optional)
- Gunicorn

**Shipped version:** 2.0

## Configuration

## Documentation

 * YunoHost documentation: https://yunohost.org/en/app_flask

## YunoHost specific features

#### Multi-users support

#### Supported architectures

* x86-64 - [![Build Status](https://ci-apps.yunohost.org/ci/logs/flask.svg)](https://ci-apps.yunohost.org/ci/apps/flask/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/flask.svg)](https://ci-apps-arm.yunohost.org/ci/apps/flask/)

## Limitations

## Additional information

#### ToDo

## Links

 * Report a bug: https://github.com/YunoHost-Apps/flask_ynh/issues
 * YunoHost website: https://yunohost.org/

---

## Developers info

Please do your pull request to the [testing branch](https://github.com/YunoHost-Apps/flask_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/flask_ynh/tree/testing --debug
or
sudo yunohost app upgrade flask -u https://github.com/YunoHost-Apps/flask_ynh/tree/testing --debug
```
