# to run: source create_buddy_table.sql;

create database study_buddy;

use study_buddy;

create table posts(post_id varchar(8) primary key, user_id int(11) not null, username varchar(30) not null, title varchar(500) not null, text_content varchar(1000) not null, course varchar(20) not null);

create table users(email varchar(40) not null, user_id int(11) primary key, username varchar(30) not null, personal_info varchar(1000));



# insert test data
insert into users
	values ("wrcastel@uci.edu", 1, "wrcastel", "This is my bio");

insert into posts
	values ("7dfsjy92", 1, "wrcastel", "Looking for a buddy", "Does anybody want to study at Ayala tonight at 4pm?", "CS143B");

# buddy_data.sql