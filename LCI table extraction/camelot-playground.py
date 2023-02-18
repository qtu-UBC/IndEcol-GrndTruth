import camelot
import os
import pandas as pd

# specify the pdf file name and identify the path
pdf_file = 'example_pdf.pdf'
pdf_file_path = os.path.sep.join([os.getcwd(),pdf_file])

# extract all the tables in the PDF file
abc = camelot.read_pdf(pdf_file_path, pages='all', flavor='stream') 

# number of tables extracted
print(abc)

# create an ExcelWriter object to write to the output file
writer = pd.ExcelWriter('example_table_extracted.xlsx', engine='xlsxwriter')

for i, table in enumerate(abc):
	table.df.to_excel(writer,sheet_name="-".join(['table',str(i)]), index=False)

# export the tables as one excel file
writer.save()