# review_challange

# Run Instructions

# This program utilizes pipenv to manage dependancies 
# To start the server, navigate to the coding challenge folder in your terminal and in the command line run "./run1.sh"
# This will start the server listening at http://127.0.0.1:8000

# Traveling to http://127.0.0.1:8000/form submits a GET request to the API and loads a form in your browser that accepts a string. 

# Entering a string submits a POST request to the API and calls get_review_list()

# get_review_list() accepts the string and passes it to fetch_review_html()

# fetch_review_html() makes a get request utilizing the string as the URL and on sucess (200) returns the response text.  On any other code, it returns an empty string

# get_review_list() takes the response and checks that it is not the empty string.  If it recieves the html, it passes it to parse_review_html().  Otherwise it returns an error.

# parse_review_html() takes the html response and parses out a list of mainReviews, passing it back to get_review_list().  If at any point parse_review_html() fails to find the classes as it parses, it will return an empty string.

# get_review_list() takes the response and check that it is not the empty string.  If it recieves the list of Reviews it passes them to review_html_to_text_list.  Otherwise it returns an error

# review_html_to_text_list takes the list of reviews and itirates over them, utilizing small functions to parse out the fields that are pertinent to this challenge.  Once it has parsed the whole list, it returns a new list of the parsed review fields.

# get_review_list takes the parsed list of reviews from review_html_to_text_list and turns them into a dict and then returns the dict to the handler which serves it to the users webpage in JSon

# Test Instructions

# To run the tests, Navigate to the coding challenge folder on your machine and run pytest
