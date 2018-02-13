"""
@author Disha Gupta
"""

# Import all of the necessary modules.
import matplotlib.pyplot as plt
import pylab
import csv

# Define a function to graph the number of retweets each tweet got.
def rts():
    
    # Store the file.
    tweets = "tweets_edited.csv"
    
    try:
        # Try to open the file.
        data = open(tweets, "r")
        
    except:
        # Print a message to the user if the file won't open.
        print("The file cannot be found.")
        
    else:    
        # Create empty lists that will store the values of the information gathered.
        # Indexes stores the indexes of each tweet.
        indexes = []
        # rtsHillary stores the number of RTs Hillary got.
        rtsHillary = []
        # rtsDonald stores the number of RTs Donald got.
        rtsDonald = []
        
        # Use the csv.reader() method to read the file.
        myCSV = csv.reader(data)
        
        # Loop through every row in the csv file.
        for row in myCSV:
            # Store the indexes.
            indexes.append(row[0])
            # Check to see if Hillary was tweeting.
            if row[2] == "HillaryClinton":
                # If she was, append the number of rts she got to the list.
                rtsHillary.append(row[10])
                # If she wasn't, append the number 0 to Donald's list.
                rtsDonald.append(0)
            # Check to see if Donald was tweeting.    
            if row[2] == "realDonaldTrump":
                # If he was, append the number of rts he got to the list.
                rtsDonald.append(row[10])
                # If he wasn't, append the number 0 to Hillary's list.
                rtsHillary.append(0)
    
        # Add the graph title.
        pylab.title("Number of RTs (Hillary vs. Donald)")
        # Plot the indexes from 2 onwards (that's where the index is 1), plot the number of RTs 
        # Hillary got, change Hillarys graph line to blue, and add a label.
        pylab.plot(indexes[2:],rtsHillary[1:], color="blue", label="Hillary RTs")
        # Plot the indexes from 2 onwards (that's where the index is 1), plot the number of RTs 
        # Donald got, change Donalds graph line to red, and add a label.
        pylab.plot(indexes[2:], rtsDonald[1:],color="red", label="Donald RTs")
        # Label the x axis.
        pylab.xlabel("# of Tweet")
        # Label the y axis.
        pylab.ylabel("# of RTs")
        # Add a legend.
        pylab.legend(loc='upper right')
        # Show the graph.
        pylab.show()
        
# Call the function.
rts()

# Define a function to graph the number of favorites each tweet got.
def favorites():
    
    # Store the file.
    tweets = "tweets_edited.csv"
    
    try:
        # Try to open the file.
        data = open(tweets, "r")
        
    except:
        # Print a message to the user if the file won't open.
        print("The file cannot be found.")
        
    else:     
        # Create empty lists that will store the values of the information gathered.
        # Indexes stores the indexes of each tweet.
        indexes = []
        # favsHillary stores the number of favorites Hillary got.
        favsHillary = []
        # favsDonald stores the number of favorites Donald got.
        favsDonald = []
        
        # Use the csv.reader() method to read the file.
        myCSV = csv.reader(data)
        
        # Loop through every row in the csv file.
        for row in myCSV:
            # Store the indexes.
            indexes.append(row[0])
            # Check to see if Hillary was tweeting.
            if row[2] == "HillaryClinton":
                # If she was, append the number of favorites she got to the list.
                favsHillary.append(row[11])
                # If she wasn't, append the number 0 to Donald's list.
                favsDonald.append(0)
            # Check to see if Donald was tweeting.
            if row[2] == "realDonaldTrump":
                # If he was, append the number of favorites he got to the list.
                favsDonald.append(row[11])
                # If he wasn't, append the number 0 to Hillary's list.
                favsHillary.append(0)
    
        # Add the graph title.
        pylab.title("Number of Favorites (Hillary vs. Donald)")
        # Plot the indexes from 2 onwards (that's where the index is 1), plot the number of favorites 
        # Hillary got, change Hillarys graph line to blue, and add a label.
        pylab.plot(indexes[2:],favsHillary[1:], color="blue", label="Hillary Favs")
        # Plot the indexes from 2 onwards (that's where the index is 1), plot the number of favorites 
        # Donald got, change Donalds graph line to red, and add a label.
        pylab.plot(indexes[2:], favsDonald[1:],color="red", label="Donald Favs")
        
        # Label the x axis.
        pylab.xlabel("# of Tweet")
        # Label the y axis.
        pylab.ylabel("# of Favs")
        # Add a legend.
        pylab.legend(loc='upper right')
        # Show the graph.
        pylab.show()
        
# Call the function.
favorites()

# Define a function that makes a pie chart based on an analysis of Donald's tweets.
def donaldTweetAnalysis():
    
     # Store the file.
    tweets = "tweets_edited.csv"
    
    try:
        # Try to open the file.
        data = open(tweets, "r")
        
    except:
        # Print a message to the user if the file won't open.
        print("The file cannot be found.")
        
    else:     
        # Create empty lists that will store the values of the information gathered.
        # Sad stores whether or not he tweeted the phrase "sad!".
        sad = []
        # Hashtags stores whether or not they used a hashtag.
        hashtags = []
        # Original Tweet checks if they wrote the tweet or not.
        originalTweet = []
        # Indexes stores the indexes of each tweet.
        indexes = []        
        
        # Use the csv.reader() method to read the file.
        myCSV = csv.reader(data)
        
        # Loop through every row in the csv file.
        for row in myCSV:
            # This list keeps track of the number of tweets made by Donald.
            if row[2] == "realDonaldTrump":
                indexes.append(1)
            else: 
                indexes.append(0)
            # Check to see if Donald was tweeting and if it was his own tweet.
            if row[2] == "realDonaldTrump" and row[4] == "True":
                # If he was, append the number 1 to the list to keep track of how many times he did.
                originalTweet.append(1)
            else:
                # Else, append the number 0.
                originalTweet.append(0)
            # Check to see if Donald was tweeting and if he said "sad!".
            if row[2] == "realDonaldTrump" and row[16] == "True":
                # If he was, append the number 1 to the list to keep track of how many times he did.
                sad.append(1)
            else:
                # Else, append the number 0.
                sad.append(0)
            # Check to see if Donald was tweeting and if he used a hashtag.
            if row[2] == "realDonaldTrump" and row[17] == "True":
                # If he was, append the number 1 to the list to keep track of how many times he did.
                hashtags.append(1)
            else:
                # Else, append the number 0.
                hashtags.append(0)

        # Calculate the percentage of original tweets out of all tweets.
        originalTweetPercentage = ( (sum(originalTweet)/sum(indexes)) * 100 )
        
        # Calculate the percentage of tweets that had the phrase "sad!" out of all tweets.
        sadPercentage = ( (sum(sad)/sum(indexes)) * 100 )
        
        # Calculate the percentage of tweets that had hashtags out of all tweets.
        hashtagsPercentage = ( (sum(hashtags)/sum(indexes)) * 100 )
        
        # Label the pie chart.
        labels = ('said "sad!" ', "original tweet", "used hashtags")
        sizes  = [sadPercentage,originalTweetPercentage,hashtagsPercentage]
        explode = [0.1,0.1,0.1]
    
        figure1, ax1 = plt.subplots()
        ax1.pie(sizes,explode=explode,labels=labels, autopct="%1.1f%%")
        # Add the graph title.
        ax1.set_title("Donald Trump Tweets Analysis")
        ax1.axis("equal")
        # Show the graph.
        plt.show()

# Call the function.
donaldTweetAnalysis()

# Define a function that makes a pie chart based on an analysis of Hillary's tweets.
def hillaryTweetAnalysis():
    
     # Store the file.
    tweets = "tweets_edited.csv"
    
    try:
        # Try to open the file.
        data = open(tweets, "r")
        
    except:
        # Print a message to the user if the file won't open.
        print("The file cannot be found.")
        
    else:           
        # Create empty lists that will store the values of the information gathered.
        # Hashtags stores whether or not they used a hashtag.
        hashtags = []
        # Original Tweet checks if they wrote the tweet or not.
        originalTweet = []
        # Indexes stores the indexes of each tweet.
        indexes = []        
        
        # Use the csv.reader() method to read the file.
        myCSV = csv.reader(data)
        
        # Loop through every row in the csv file.
        for row in myCSV:
            # This list keeps track of the number of tweets made by Hillary.
            if row[2] == "HillaryClinton":
                indexes.append(1)
            else: 
                indexes.append(0)
            # Check to see if Hillary was tweeting and if it was her own tweet.
            if row[2] == "HillaryClinton" and row[4] == "True":
                # If she was, append the number 1 to the list to keep track of how many times she did.
                originalTweet.append(1)
            else:
                # Else, append the number 0.
                originalTweet.append(0)
            # Check to see if Hillary was tweeting and if she used a hashtag.
            if row[2] == "HillaryClinton" and row[17] == "True":
                # If she was, append the number 1 to the list to keep track of how many times she did.
                hashtags.append(1)
            else:
                # Else, append the number 0.
                hashtags.append(0)
        
        # Calculate the percentage of original tweets out of all tweets.
        originalTweetPercentage = ( (sum(originalTweet)/sum(indexes)) * 100 )

        # Calculate the percentage of tweets that had hashtags out of all tweets.
        hashtagsPercentage = ( (sum(hashtags)/sum(indexes)) * 100 )
        
        # Label the pie chart.
        labels = ("original tweet", "used hashtags")
        sizes  = [originalTweetPercentage,hashtagsPercentage]
        explode = [0.1,0.1]
    
        figure1, ax1 = plt.subplots()
        ax1.pie(sizes,explode=explode,labels=labels, autopct="%1.1f%%")
        # Add the graph title.
        ax1.set_title("Hillary Clinton Tweets Analysis")
        ax1.axis("equal")
        # Show the graph.
        plt.show()

# Call the function.
hillaryTweetAnalysis()
