# f_analysis

This program allows users to run basic EBITDA and DCF analysis. It takes in data from spreadsheets
(csv, xls, xlsx) and outputs a csv with the desired output analysis. This program handles folders 
on Mac systems.

## EBITDA

For EBITDA, the spreadsheets should have the total sales, operating expenses or losses, and total losses.
The corresponding script for EBITDA is f_analysis.py.

## DCF

For DCF, the spreadsheets should have free cash flow (FCF), Discount Rate, Cash and Equivalents, Debt, Shares
Oustanding, Cas Flow From Operations, expected growth for current year (Expected Growth), and expected capital 
expenditures for current year (Expected CapEx). The corresponding script for DCF is f_analysis2.py.

The DCF analysis is done based on the previous fiscal year, based on expected growth, and based on both
expected growth and the discount rate.

## base.py

This is where the user runs the program from. When ran, the user is prompted to enter 1, 2, or 3.
Each number corresponds to an analysis calculation: 1 is for EBITDA, 2 is for DCF, and 3 is for
both.

## Folder Arrangement

The user should create two folders, Input and Output. In the Input folder, the user should have the
spreadsheet that will serve as an input. If using xls or xlsx, the EBITDA input data should be on
the first tab and DCF input data on the second tab. If using csv and the user wishes to perform 
both EBITDA and DCF analyses, they would need to use one csv input file for each. Place the EBITDA
input file in the Input folder, and once the EBITDA analysis is complete, replace it with the DCF
input file.

Before performing any analyses, update lines 6, 11, and 17 of f_analysis.py and f_analysis2.py 
with the directory of the Input folder. In f_analysis.py, update lines 35 and 39 with the directory
of the Output folder. In f_analysis2.py, update lines 72 and 76 with the directory of the Output
folder.

## Dependencies

pip install pandas
pip install os
pip install sys
pip install subprocess

## TODO

For the future, I have planned to make it possible to analyze multiple input files, and Windows folders. Also planned, is
adding the ability to run DCF analysis out to 5 and 10 years.