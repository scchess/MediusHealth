#
# Clean up the data for machine learning challenge
#

import re
from xlrd import open_workbook

for sheet in open_workbook('machine_learning_challenge.xlsx').sheets():
    for row in range(0, sheet.nrows):
        for col in range(sheet.ncols):
            # Use lower cases (e.g. 'Life' == 'life)
            x = sheet.cell(row,col).value.lower().strip()

            # Remove unnecessary spaces/new lines
            x = x.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')

            def transform(x):            
                x = "\n".join([line for line in x.split('\n') if line.strip() != ''])
            
                # Remove common stopwords (e.g. "degree" == "degree.")
                x = x.replace('.', '').replace('?', '').replace('!', '').replace(',', '')

                return re.sub(' +', ' ', x)

            x = "\n".join([transform(line) for line in x.split('\n') if line.strip() != ''])        
            
            print(x, end='')

            # Convert output to TSV format
            if col == 0:
                print('\t', end='')
        print()