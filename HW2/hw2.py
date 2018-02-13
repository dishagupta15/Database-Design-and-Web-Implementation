"""
@author: Disha Gupta
"""

# Import the Python "Pandas" module to use to clean the dataset
import pandas as pd
# Import other necessary modules.
import datetime

# Store the file name
tweetsFile = "tweets.csv"

# Store the data frame
df = pd.read_csv(tweetsFile)

# Delete unnecessary columns from the data frame
del df["in_reply_to_status_id"]
del df["in_reply_to_user_id"]
del df["longitude"]
del df["latitude"]
del df["place_id"]
del df["place_full_name"]
del df["place_name"]
del df["place_type"]
del df["place_country_code"]
del df["place_country"]
del df["place_contained_within"]
del df["place_attributes"]
del df["place_bounding_box"]
del df["source_url"]
del df["truncated"]
del df["entities"]
del df["extended_entities"]

# Use the time column to make a new column to determine if Hillary or Donald tweeted between midnight and 6 am.
# This can be done using lambda functions.
df["time"] = df.time.apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'))
df["tweeted_between_12am_and_6am"] = df["time"].apply(lambda x: x.hour < 6 or x.hour > 24) 

# Search for the string "Donald" or "Trump" inside of Hillary's tweets to see if she mentions him.
# Set the parameter for case to False so that the search is case insensitive.
# If a match is found, create a new column at the end called which will store the boolean value of the result.
# Also, check to see if the user tweeting is Hillary.
df["hillary_mentions_donald"] = (df.iloc[:, 2].str.contains("Donald|Trump" , case=False)) & (df.handle == "HillaryClinton")

# Search for the string "Hillary" or "Clinton" inside of Donalds's tweets to see if he mentions her.
# Set the parameter for case to False so that the search is case insensitive.
# If a match is found, create a new column at the end called which will store the boolean value of the result.
# Also, check to see if the user tweeting is Donald.
df["donald_mentions_hillary"] = (df.iloc[:, 2].str.contains("Hillary|Clinton" , case=False)) & (df.handle == "realDonaldTrump")
 
# Make a column that counts the number of characters in the tweet.
df["character_count"] = df.text.apply(len)

# Make a column to see when Donald Trump tweets the phrase "sad!".
df["sad!"] = df.iloc[:, 2].str.contains("sad[!]{1}" , case=False)

# Make a column to see when the Hillary or Donald use a hashtag in their tweets.
df["hashtags"] = df.iloc[:, 2].str.contains("[#]{1}" , case=False)

# Output the new dataset to a new csv file.
df.to_csv("tweets_edited.csv")
