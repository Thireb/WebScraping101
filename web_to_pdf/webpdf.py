import pandas as pd
import pdfkit as pk
df = pd.read_excel('test.xlsx')
links = df['link']
filenames = df['file must be named']
pk.from_url(links[1],filenames[1])
print(links[0])
