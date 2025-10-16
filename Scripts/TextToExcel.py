import pandas as pd

# Read the text file
df = pd.read_csv(r'C:\Users\dadaskalopoulos\Downloads\Enhance-Email-Templates-to-Include-Contract-ID.txt', delimiter='\t')  

# Save to Excel
df.to_excel('Enhance-Email-Templates-to-Include-Contract-ID.xlsx', index=False)