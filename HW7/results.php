<?php

// Set up the page title.
echo "<head><title>Harry Styles Solo Career Quiz</title> <link rel='stylesheet' type='text/css' href='layout.css'> </head>";

// Add a header.
echo "<h3> Harry Styles Solo Career Quiz Results: </h3>";

// Add in the picture.
echo "<img src='http://orig08.deviantart.net/f138/f/2015/222/8/d/harry_styles_png_by_shabush2812-d9522an.png' alt='Harry Styles'>";

// Get all of the users answers and store them.
$answer1 = $_POST['question-1-answers'];

$answer2 = $_POST['question-2-answers'];

$answer3 = $_POST['question-3-answers'];

$answer4 = $_POST['question-4-answers'];

$answer5 = $_POST['question-5-answers'];

$answer6 = $_POST['question-6-answers'];

// Make a variable to store the total number of correct answers the user picked.
$totalCorrect = 0;

// Go through the users answers and see which ones they answered correctly.
// If one of their answers is correct, add 1 to the counter variable.
if ($answer1 == "D") { $totalCorrect++; }

if ($answer2 == "A") { $totalCorrect++; }

if ($answer3 == "B") { $totalCorrect++; }

if ($answer4 == "D") { $totalCorrect++; }

if ($answer5 == "C") { $totalCorrect++; }

if ($answer6 == "B") { $totalCorrect++; }

// Print out the users results.
echo "<div id='results'> You got $totalCorrect out of 6 correct! </div>";

// Print out a special message for each possible outcome the user could have had.
if ($totalCorrect == 0) {
	echo "That was awful!";
}

if ($totalCorrect == 1) {
	echo "That was okay...";
}

if ($totalCorrect == 2) {
	echo "At least you've heard of Harry :(";
}

if ($totalCorrect == 3) {
	echo "You're getting there!";
}

if ($totalCorrect == 4) {
	echo "I'm guessing you're a fan of Harry!";
}

if ($totalCorrect == 5) {
	echo "That was great!";
}

if ($totalCorrect == 6) {
	echo "That was amazing! You know Harry so well :')";
}

echo "<br>";
echo "<br>";

// Print out a results breakdown.
echo "Results Breakdown:";

echo "<br>";
echo "<br>";

// Tell the user all of the correct answers and check if they got it right or wrong.
echo "The answer to #1 is D. You put $answer1. ";
if ($answer1 == "D") { echo "You got it right! <br>"; }
else { echo "You got it wrong :'( <br>"; }

echo "The answer to #2 is A. You put $answer2. ";
if ($answer2 == "A") { echo "You got it right! <br>"; }
else { echo "You got it wrong :'( <br>"; }

echo "The answer to #3 is B. You put $answer3. ";
if ($answer3 == "B") { echo "You got it right! <br>"; }
else { echo "You got it wrong :'( <br>"; }

echo "The answer to #4 is D. You put $answer4. ";
if ($answer4 == "D") { echo "You got it right! <br>"; }
else { echo "You got it wrong :'( <br>"; }

echo "The answer to #5 is C. You put $answer5. ";
if ($answer5 == "C") { echo "You got it right! <br>"; }
else { echo "You got it wrong :'( <br>"; }

echo "The answer to #6 is B. You put $answer6. ";
if ($answer6 == "B") { echo "You got it right! <br>"; }
else { echo "You got it wrong :'( <br>"; }

?>