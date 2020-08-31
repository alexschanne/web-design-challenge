#importing dependencies
import pandas as pd 

#reading csv with pandas into a html code
df = pd.read_csv('../Resources/weather_data.csv')
df.to_html('data.html', index=False)
table= df.to_html()

#save output to file to copy for html page
f= open("output.txt", "a")
print(table, file=f)
f.close()
