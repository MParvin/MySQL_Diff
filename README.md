# MySQL_Diff
Find differents between MySQL master,slave or master,master databases.

To use this program just copy `.env.example` to `.env`
```
cp .env.example .env
```

Edit `.env` and put your database credentials.

## Env file and examples

#### IP address of Master Database
```database_master = '192.168.1.100'```
#### IP address of second server (Slave or Master)
```database_slave  = '192.168.1.101'```
#### Which database you want to check sync status
```database_name   = 'wordpress_db'```
#### User who has SELECT privileges on the database
```database_user   = 'wp_db_user'```
#### User password
```database_pass   = 'SECURE_PASSWORD'```
#### Where you want to log output
```log_file        = '/var/log/db_diff.log'```
####  eed to sleep, because syncing is not fast in some cases
```max_time_to_sync = 20```


## Dependencies

Install dependencies:
```
pip install -r requirements.txt
```
***Attention:*** Use [virtualenv](https://pypi.org/project/virtualenv/)

## Start app

To run the app, use:
```
python main.py
```

I recommened you use [screen](https://linux.die.net/man/1/screen), if you have a large database;

## Security

And instead of using `root` user create a readonly user:
###### Mariadb
```
create user anyone@'%' identified by 'SECURE_PASSWORD';
grant SELECT TO anyone@'%';
```

###### MySQL 8
```
create user anyone@'%';
grant SELECT TO anyone@'%' identified by 'SECURE_PASSWORD';
```
