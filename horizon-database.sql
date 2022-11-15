-- Get connection info
\conninfo

-- Create user with password
sudo -u postgres psql
create user nuclear;
alter user nuclear password 'placeholder';

-- Create database
create database spider001;

-- Create the table
create table horizon001(
    id serial unique,
    link varchar(150),
    visited integer,
    primary key (id)
);

-- Check table details
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    CHARACTER_MAXIMUM_LENGTH AS MAX_LENGTH, 
    CHARACTER_OCTET_LENGTH AS OCTET_LENGTH 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'horizon001';

-- Create md5 hashed index
CREATE UNIQUE INDEX link_md5 ON horizon001(MD5(link));

-- Insert seed horizon (sample command)
insert into horizon001 (link, visited) values ('meow',0);

-- Check if index scan is working
EXPLAIN ANALYZE SELECT * FROM horizon001 WHERE md5(link) = md5('meow');

