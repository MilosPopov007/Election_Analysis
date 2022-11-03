# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who recived votes
#3. The precentage of votes each candidate won
#4. The total number of votes each candidate won
5#. The winner of the election based on popular vote.

# Read Data from the file
# Indirect Path to the File
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct path to the file. (first make analysis folder in Election_Analysis to crear output folder and Python will make election_analysis.txt file )
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")

# Create a file name variable to direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file
outfile = open( file_to_save, "w")
# write some data to the file
outfile.write("Hello World")
#Close the file (in order to save data)
outfile.close()

#CODE for writing a file using "with" statement (to be clean and more concise)
# Create a file name to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the "with statement" open the file as a text file
with open(file_to_save, "w") as txt_file:
    # write some data to the file
    

    # write three countis to the file (Arapahoe, Denver, Jefferson) make sure that they are separated by comma and a space to look good
    txt_file.write("Arapahoe, Denver, Jefferson")

    # If we want to write each conty on a separate line use : \n (Everything after \n will be on the next line)
    # txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies
import csv
import os
# Assign a variable to load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open election results and read a file, don't forget to add a colon after the with statement and indent on the next line.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here. This will allow us to read the CSV file using the csv module with the reader function.
    # Read the file object with reader function
    file_reader = csv.reader(election_data)
    
   
    # Print the header row
    headers = next(file_reader)
    print(headers)
# Commiting code to Git Bash, Windows gives you an option to open git bash from your working directory by right-clicking on your folder and selecting GitBash here
# This way you commit your code to your Github repository, In Git Bash, you will know that you are in a tracked GitHub repository when the folder has (main) after the folder name
