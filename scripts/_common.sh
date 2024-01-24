#!/bin/bash

#=================================================
# SET CONSTANTS
#=================================================

log_path=/var/log/$app
log_file="${log_path}/${app}.log"

#=================================================
# HELPERS
#=================================================

myynh_setup_python_venv() {
    # Always recreate everything fresh with current python version
    ynh_secure_remove "$install_dir/venv"

    # Skip pip because of: https://github.com/YunoHost/issues/issues/1960
    python3 -m venv --without-pip "$install_dir/venv"

    chown -c -R "$app:" "$install_dir"

    # run source in a 'sub shell'
    (
        set +o nounset
        source "$install_dir/venv/bin/activate"
        set -o nounset
        set -x
        ynh_exec_as $app $install_dir/venv/bin/python3 -m ensurepip
        # using --no-cache-dir option because user doesn't have permission to write on cache directory (don't know if it's on purpose or not)
        ynh_exec_as $app $install_dir/venv/bin/pip3 install --no-cache-dir --upgrade wheel pip setuptools
        ynh_exec_as $app $install_dir/venv/bin/pip3 install --no-cache-dir -r "$install_dir/requirements.txt"
    )
}

myynh_setup_log_file() {
    (
        set -x

        mkdir -p "$(dirname "$log_file")"
        touch "$log_file"

        chown -c -R $app:$app "$log_path"
        chmod -c o-rwx "$log_path"
    )
}

myynh_fix_file_permissions() {
    (
        set -x

        # /home/yunohost.app/$app/
        chown -c -R "$app:" "$data_dir"
        chmod -c o-rwx "$data_dir"

        # /var/www/$app/
        chown -c -R "$app:" "$install_dir"
        chmod -c o-rwx "$install_dir"
    )
}