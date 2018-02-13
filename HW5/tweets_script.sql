DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets (
	id int NOT NULL,
	handle varchar,
	tweet varchar,
	is_retweet varchar,
	original_author varchar,
	time_stamp date,
	in_reply_to_screen_name varchar,
	is_quote_status varchar,
	lang varchar,
	retweet_count int,
	favorite_count int,
	tweeted_between_12am_and_6am varchar,
	hillary_mentions_donald varchar,
	donald_mentions_hillary varchar,
	character_count int,
	sad varchar, 
	hashtags varchar,
	PRIMARY KEY (id)
);