# Python-Challenge

## PyBank 

The PyBank application reads from a csv file the list of values corresponding to this format: column 1 = date formatted as month and year, column 2 = profit as positive value and loss as a negative value. 
PyBank stores the dates and profit values in separate lists. In a third list, PyBank stores the change from month to month.
PyBank then calculates the greatest profit and loss.
PyBank also stores the date of these two values
PyBank next calculates and stores the average of the change over time in profit/loss.
Lastly, PyBank prints these values to the console and writes them to a text file.

## PyPoll 

The PyPoll application reads from a csv file the list of values corresponding to this format: column 1 = Ballot ID formatted as number, column 2 = County as a string, and column 3 = Candidate name as a string
PyPoll stores the total votes in a list of strings of candidate names by looping through the entire csv going through column 3. This list is then sorted to put the same candidate names together.
PyPoll set stores the unique list of candidate names.
PyPoll then stores the raw votes for each candidate.
PyPoll next calculates and stores the percentage of votes for each candidate.
PyPoll finally prints and writes the total votes and vote percentage with each candidate name.