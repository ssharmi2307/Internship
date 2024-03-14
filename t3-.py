
import pandas as pd

# Load the raw data from CSV into a pandas DataFrame
raw_data = pd.read_excel("rawdata.xlsx")

# Assuming the raw data has columns 'date', 'number', 'activity', 'position', and 'location'
# We'll rename the columns to match the desired output
raw_data = raw_data.rename(columns={'date': 'Date', 'activity': 'Activity', 'position': 'Position','number':'Number'})


# 1. Datewise total duration for each inside and outside
# Check if 'inside' and 'outside' are present in the Position column
if 'inside' in raw_data['Position'].unique() and 'outside' in raw_data['Position'].unique():
    # Calculate the duration for each position
    duration_by_position = raw_data.groupby(['Date', 'Position']).size().unstack(fill_value=0)

    # Splitting into inside and outside durations if they exist
    inside_duration = duration_by_position['inside'] if 'inside' in duration_by_position.columns else 0
    outside_duration = duration_by_position['outside'] if 'outside' in duration_by_position.columns else 0
else:
    # If 'inside' and 'outside' are not present, set durations to 0
    inside_duration = 0
    outside_duration = 0

# 2. Datewise number of picking and placing activity done
# We'll count the occurrences of picking and placing activities for each date
activity_count = raw_data.groupby(['Date', 'Number']).size().unstack(fill_value=0)

# Merge both results into a single DataFrame
result = pd.DataFrame({
    'Date': activity_count.index,
    'pick_activities': activity_count['picked'] if 'picked' in activity_count.columns else 0,
    'place_activities': activity_count['placed'] if 'placed' in activity_count.columns else 0,
    'inside_duration': inside_duration,
    'outside_duration': outside_duration
})

# Save the result to an output CSV file
result.to_csv("output.csv", index=False)

