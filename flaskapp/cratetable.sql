.tables :
shows all tables in the database

.schema tablename :
look at the structure of the table 

create table:

CREATE TABLE users (
 contact_id integer PRIMARY KEY,
 name text NOT NULL,
 email text NOT NULL UNIQUE,
 password text NOT NULL
);

insert data into the table:
INSERT INTO users (name,email,password) VALUES ('abdullah','aaa@aaa.com','123456');

select data:
select * from users ;


user guide :

