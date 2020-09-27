import pandas as pd
import bar_chart_race as bcr

# Stores CSV file name. 
file_name = "hot100.csv"

# Reads CSV into a panda's data frame. 
data_frame = pd.read_csv(file_name)

# Formats  data into wide data using a cumulative sum pivot table.
wide_data = data_frame.pivot_table(index='Week', columns='Performer', aggfunc='count', fill_value=0).cumsum()

# Removes generated header from pivot table.
wide_data.columns = wide_data.columns.droplevel(0)

# Drop the index column from wide data dataframe.
wide_data.reset_index(drop=True, inplace=True)

# Removes duplicate columns.
wide_data = wide_data.loc[:,~wide_data.columns.duplicated()]

# Prepare sub-dataset with data on artists to "race" in animation.
columns = [ "Madonna", "Michael Jackson", "Drake", "Rihanna", "Lady Gaga"]
sub_dataset = wide_data[columns]

# Racing Time! Creates the bar chart mp4 file.
bcr.bar_chart_race(sub_dataset, filename='hot100.mp4')

