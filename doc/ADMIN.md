To customize the Flask app, you have to put your code in `__DATA_DIR__/flask-app/`

Your code must have a '__init__'.py file and the Flask object must be named 'app'

Logs are available in file `/var/log/__APP__/__APP__.log`.

After manual changes in source code, restart Flask: `service __APP__ restart`.

To access source code via SFTP or SSH, log-in with user `__APP__` and the password set during installation. 

If you want to access virtualenv, for exemple to manually install PIP dependencies:

```
bash
cd /var/www/__APP__/
. venv/bin/activate
```
