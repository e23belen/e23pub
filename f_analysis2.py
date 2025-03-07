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
        df = pd.read_excel(filename, 1)
except ValueError:
    print("Wrong file type.")

fcf = df['FCF']
discount_rate = df['Discount Rate']
cash_and_equivalents = df['Cash and Equivalents']
debt = df['Debt']
shares_outstanding = df['Shares Outstanding']

cash_flow_from_operations = df['Cash Flow From Operations']
expected_growth = df['Expected Growth']
expected_capex = df['Expected CapEx']

# Simple DCF
present_value_of_a_perpetuity = fcf/discount_rate
equity_value = present_value_of_a_perpetuity + cash_and_equivalents - debt
value_per_share = equity_value/shares_outstanding

# Simple DCF based on expected growth
expected_cash_flow = cash_flow_from_operations * (1 + expected_growth)
expected_fcf = expected_cash_flow - expected_capex
present_value_of_a_perpetuity_2 = expected_fcf/discount_rate
expected_equity_value = present_value_of_a_perpetuity_2 + cash_and_equivalents - debt
expected_value_per_share = expected_equity_value/shares_outstanding

# Simple DCF based on difference between discount and growth rate
present_value_of_growing_perpetuity = expected_fcf/(discount_rate - expected_growth)
expected_equity_value_2 = present_value_of_growing_perpetuity + cash_and_equivalents - debt
expected_value_per_share_2 = expected_equity_value_2/shares_outstanding

df['Present Value of a Perpetuity'] = present_value_of_a_perpetuity.round(2)
df['Equity Value'] = equity_value.round(2)
df['Value Per Share'] = value_per_share.round(2)

df['Expected Cash Flow'] = expected_cash_flow.round(2)
df['Expected FCF'] = expected_fcf.round(2)
df['Present Value of a Perpetuity CY'] = present_value_of_a_perpetuity_2.round(2)
df['Expected Equity Value'] = expected_equity_value.round(2)
df['Expected Value Per Share'] = expected_value_per_share.round(2)

df['Present Value of Growing Perpetuity'] = present_value_of_growing_perpetuity.round(2)
df['Expected Equity Value GP'] = expected_equity_value_2.round(2)
df['Expected Value Per Share GP'] = expected_value_per_share_2.round(2)

# Add the directory for the output folder
i = 1
while os.path.exists('/dcf_output_%s.csv' % i):
    i += 1

# Add the directory for the output folder
df.to_csv('/dcf_output_%s.csv' % i)