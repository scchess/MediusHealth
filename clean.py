#
# Clean up the data for machine learning challenge
#

from xlrd import open_workbook

for sheet in open_workbook('machine_learning_challenge.xlsx').sheets():
    for row in range(0, sheet.nrows):
        for col in range(sheet.ncols):
            x = sheet.cell(row,col).value.strip()
            
            # Simple data transformation
            x = x.replace('\r', '').replace('\n', '').replace('\t', ' ')

            if col == 0:
                # Remove periods from the category column. E.g: "Low Blood Preasure." to ""Low Blood Preasure".
                x = x.replace('.', '')                
    
            print(x, end='')

            # Convert output to TSV format
            if col == 0:
                print('\t', end='')
        print()