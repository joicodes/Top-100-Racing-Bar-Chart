import pandas as pd
import bar_chart_race as bcr


# Step 1: Store CSV file name 
file_name = "hot100.csv"

# Step 2: Read CSV into a panda's data frame 
data_frame = pd.read_csv(file_name)
#print(data_frame.head())

# Step 3: Format your data into wide data using a cumulative sum pivot table
wide_data = data_frame.pivot_table(index='Week', columns='Performer', aggfunc='count', fill_value=0).cumsum()
#print(wide_data.head())

# Step 4: Remove Generated Header
wide_data.columns = wide_data.columns.droplevel(0)
print(wide_data.head())


# Step 5: Remove Duplicate Columns
wide_data = wide_data.loc[:,~wide_data.columns.duplicated()]
print(wide_data.head())


# Step 6: Prepare sub data set with data on artists we want to race.
columns = [ "Madonna", "Michael Jackson", "Drake", "Rihanna", "Lady Gaga"]
sub_dataset = wide_data[columns]
print(sub_dataset.head())

sub_dataset.to_csv(r'sub_dataset.csv', index=False, header=True)

# Step 7: Create Racing Bar Chart
df = pd.read_csv('sub_dataset.csv')
bcr.bar_chart_race(df, filename='hot100.mp4')

# # Step 11: Write sub data set to file:
# print("Writing sub dataset to CSV file.  Please wait....")
# sub_dataset.to_csv(r'sub_dataset.csv', index =True, header=True)
# print("Done. ✅")
