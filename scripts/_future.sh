
#=================================================
# SQLITE HELPERS
#=================================================

#TODO: Open and execute

# Create a sqlite database file
#
# usage: ynh_sqlite_create_db db
# | arg: db - the database name to create
# TODO: password protection
ynh_sqlite_create_db() {
    sqlite3 <<< ".save /var/www/$1/$1.sqlite3"
}

# Drop a database
#
# usage: ynh_sqlite_drop_db db
# | arg: db - the database name to drop
ynh_sqlite_drop_db() {
    shred /var/www/$1/$1.sqlite3
}

# Dump a database
#
# example: ynh_sqlite_dump_db 'roundcube' > ./dump.sql
#
# usage: ynh_sqltie_dump_db db
# | arg: db - the database name to dump
# | ret: the sqlitedump output
ynh_sqlite_dump_db() {
    sqlite3 /var/www/$1.sqlite3 <<< ".dump"
}

#TODO: Test
