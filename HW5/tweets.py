#!/usr/local/pkg/python/3.6.1/bin/python3

"""
@author: dishagupta
"""

import cgi
import sqlite3
import cgitb

cgitb.enable()

print ("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Clinton and Trump Tweets</title>")
print('<link rel="stylesheet" href="tweets.css" type="text/css"/>')
print("</head>")
print("<body>")
print("<h3>Hillary Clinton and Donald Trump Tweets (January 2016 to September 2016)</h3>")
print("<hr/>")

# Get the users selections
form = cgi.FieldStorage()

if "author" in form:
    author = form["author"].value
    
if "favorites" in form:
    favorites  = form["favorites"].value

print ( "<h4>"+ author + "'s Tweets Favorite Count:" +"<br>\n")
if "author" in form:
    author = form["author"].value
    print()
print ("<hr />")

# Set up a connection to sqlite3 to access the tweets.db database
connection = sqlite3.connect("tweets.db")
c = connection.cursor()

if author == "HillaryClinton" or "realDonaldTrump":
    if favorites == "Lowest 15 Tweets":
        query = "SELECT handle, favorite_count, tweet, character_count tweet FROM tweets WHERE handle ='" + author + "' ORDER BY favorite_count ASC LIMIT 15"
    elif favorites == "Highest 15 Tweets":
        query = "SELECT handle, favorite_count, tweet, character_count tweet FROM tweets WHERE handle ='" + author + "' ORDER BY favorite_count DESC LIMIT 15" 

# Execute the query
print("<p><em>Query:  </em>"+ query +"</p>")
c.execute(query)

print("<table>")
print("<tr>")
print('\t<td style="padding-right:50px;"><b>Handle</b></td>')
print('\t<td style="padding-right:50px;"><b>Favorites</b></td>')
print('\t<td style="padding-right:50px;"><b>Tweet</b></td>')
print('\t<td style="padding-right:50px;"><b>Characters</b></td>')
print("</tr>")
for handle,favorites,tweet, character_count in c:
    print("<tr>")
    print('\t<td style="padding-right:50px;">'+handle+"</td>")
    print('\t<td style="padding-right:50px;">'+ str(favorites) +"</td>")
    print('\t<td style="padding-right:65px;">'+ tweet +"</td>")
    print('\t<td style="padding-right:65px;">'+ str(character_count) +"</td>")
    print("</tr>")
print("</table>")

c.close()

print("</body>")
print("</html>")