import sys
import pandas as pd
import os

# Add the directory for the input folder
os.chdir('')

extensions_list = ['.csv', '.xls', '.xlsx']

# Add the directory for the input folder
file_direc = len(os.listdir(''))

if file_direc < 2:
    sys.exit("No file in directory")

# Add the directory for the input folder
filename = os.listdir('')[1]
file_extension = os.path.splitext(filename)[1]

try:
    index = extensions_list.index(file_extension)
    if index == 0:
        df = pd.read_csv(filename)
    else:
        df = pd.read_excel(filename, 0)
except ValueError:
    print("Wrong file type.")

EBITDA = df['Total Sales'] + df['Total Operating Expenses or Losses'] - df['Total Expenses']

df['EBITDA'] = EBITDA

# Add the directory for the output folder
i = 1
while os.path.exists('/ebitda_output_%s.csv' % i):
    i += 1

# Add the directory for the output folder
df.to_csv('/ebitda_output_%s.csv' % i)