<!DOCTYPE html>

<html>

	<head>
		<title>Tweets Swearch</title>
		
		<link rel="stylesheet" href="tweets.css" type="text/css">

	</head>

	<body>

			<h3>Tweets Search</h3>

			<form method="post" action="tweets.php">
				<select name="sort_by">

					<?php
						if (isset($_POST["sort_by"])) {
							print '<option value=" ' . $_POST['sort_by'] . ' ">' . $_POST['sort_by'] . "</option>\n";
						}
					?>

					<option value="handle">User</option>
					<option value="retweet_count">Retweet Count</option>
					<option value="favorite_count">Favorite Count</option>

				</select>
				<input type="submit" value="Search">
			</form>

		<?php

		if (isset($_POST["sort_by"]) || isset($_GET["sort_by"])) {


			if (isset($_POST['sort_by'])) {
				$sort_by = $_POST['sort_by'];
			}
			else {
				$sort_by = $_GET['sort_by'];
			}

			// Include the configuration file.
			include('/home/dg2703/protected/config.php');

			// Connect to the server.
			$db_link = new mysqli($db_server, $db_user, $db_password , $db_name);

			// Check if the server is up.
			if ($db_link->connect_errno) {
				print "This is bad ... server is down. Try again later!";
				exit;
			}
			// If the connection was successful, perform the queries.
			else {
				// Store the query in a variable.
				$sql = "SELECT * FROM tweets ORDER BY " . $sort_by . " DESC LIMIT 50";

				$record_set = mysqli_query($db_link, $sql);

				$num_records = mysqli_num_rows($record_set);

				// Print out the pictures.
				print '<div id="images">';
				print '<img src="http://freepngimages.com/wp-content/uploads/2016/04/hillary-clinton-transparent-background.png" alt="Clinton" 
					style="width:350px; height:300px; padding:10px; padding-left:85px; padding-right:10px;">';
				print '<img src="https://img.clipartfest.com/3ca714319861d6d0f53f9b7b4f5971fc_new-twitter-logo-transparent-twitter-clipart-transparent_518-518.png" alt="Twitter Logo" style="width:350px; height:300px; padding:10px; padding-right:10px;">';
				print '<img src="http://pngto.com/wp-content/uploads/2016/10/Donald-Trump-png-high-quality.png" alt="Trump" style="width:350px; height:300px; padding:10px;">';
				print '</div>';

				// Tell the user how many records there are.
				print "There are " . $num_records . " records that came back.";
				print "<br>";
				print "<br>";

				// If no records were reported, tell the user.
				if ($num_records == 0) {
					print "Sorry, no data came back.";
					print "<br>";
				}
				// Else, form the table with the selected records.
				else {
					print "<table> \n";
					print '<tr id="header">
						   <td><a href="tweets.php?sort_by=handle">User</a></td>
						   <td><a href="tweets.php?sort_by=retweet_count">Retweet Count</a></td>
						   <td><a href="tweets.php?sort_by=favorite_count">Favorite Count</a></td>
						   </tr>';

					while ($row = mysqli_fetch_array($record_set)) {
						$handle = $row['handle'];
						$retweet_count = $row['retweet_count'];
						$favorite_count = $row['favorite_count'];

						print "<tr><td>" . $handle . "</td><td>" . $retweet_count . "</td><td>" . $favorite_count . "</td></tr>";
					}

					print "</table>";
				}
			}
		}

		?>

	</body>

</html>