Pour personnaliser l'application Flask, il faut mettre votre code dans `__DATA_DIR__`/flask-app/

Votre code doit contenir un fichier __init__.py et l'objet Flask doit s'appeler 'app'.

Les logs sont disponibles dans le fichier `/var/log/__APP__/__APP__.log`.

Pour redémarrer l'application après des changements manuels, `service __APP__ restart`.

Pour accéder aux fichiers de l'application en SSH ou SFTP, utilisez l'utilisateur `__APP__` avec que le mot de passe défini lors de l'installation. 

Si vous souhaitez accéder au virtualenv, par exemple pour installer manuellement des dépendances PIP :

```
bash
cd /var/www/__APP__/
. venv/bin/activate
```
