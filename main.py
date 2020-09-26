import pandas as pd
import bar_chart_race

print()
data_set = pd.read_csv("hot100.csv")

# Set the index to be the date

print("Creating cumultive sum pivot table. Please wait....")
wide_data = data_set.pivot_table(index='WeekID', columns='Performer', aggfunc='count', fill_value=0).cumsum()
print("Done. ✅")


print("Creating wide_data.csv! Please wait....")
wide_data.to_csv(r'wide_data.csv', index = False, header=True)
print("Done. ✅")
