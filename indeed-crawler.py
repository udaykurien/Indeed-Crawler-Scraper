# Import libraries
import psycopg2
import cloudscraper
import sys
import os

# Set custom path for secrets
sys.path.insert(0,"/home/nuclear/Github/PythonPrograms/Secrets")

# Connect to database
import crawler_pg_secrets as p
pg_params = {
    'host' : p.host,
    'user' : p.user,
    'dbname' : p.dbname,
    'password' : p.password,
    'port' : p.port
}
conn =  psycopg2.connect(**pg_params)
conn.commit()
cur = conn.cursor()

table_name = 'indeed_horizon'

# Drop previous horizon table
sql_cmnd = "drop table " + table_name + ";"
try:
    cur.execute(sql_cmnd)
    print('success: ' + sql_cmnd)
except:
    print('FAIL: ' + sql_cmnd)
conn.commit()
# Create new horizon table
sql_cmnd = "create table "\
    + table_name\
    + " (id serial, url varchar(256), visited integer);"
try:
    cur.execute(sql_cmnd)
    print('success: ' + sql_cmnd)
except:
    print('FAIL: ' + sql_cmnd)
conn.commit()

# Add starting url to table
url='https://ca.indeed.com'