from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

# Set the max column width to absurd number due to html code in cell
pd.options.display.max_colwidth = 10000

# Ask user for file path
filepath = input("Enter the full file path, including file name and file extension of the file: \n")

# Create the data frame

df = pd.read_csv(str(filepath), usecols=["Title","NoteHTML"])

with open('notes.txt', 'a+') as f:
    for row in df.values:
    
        # Set variable to the html content of each cell
        html_code = row[1]
        soup = BeautifulSoup(html_code, "html.parser")

        # Write raw text content, which was extracted from html code, to file
        f.write(soup.get_text('\n'))

        # Separate each original file for organization
        f.write('\n\n--------------------------------------------- \n\n')
