from shiny import App, render, ui
import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets

# Loading the dataset
def load_data():
    url = "https://raw.githubusercontent.com/nimratmann/datasci_4_web_viz/main/datasets/PLACES__Local_Data_for_Better_Health__County_Data_2023_release.csv"
    return pd.read_csv(url)

df = load_data()

# Filtering for condition "Arthritis" as measureid and 'Crude prevalence' as data_value_type
df_arthritis = df[(df['MeasureId'] == 'ARTHRITIS') & (df['Data_Value_Type'] == 'Crude prevalence')]

# Grouping by the 'LocationName' and getting the average 'Data_Value'
grouped = df.groupby('LocationName')['Data_Value'].mean().sort_values(ascending=False)

# Plotting the data
plt.figure(figsize=(10, 7))
grouped.plot(kind='bar', color='pink')
plt.ylabel('Average Crude Prevalence (Data Value)')
plt.xlabel('County')
plt.title('Arthritis Crude Prevalence by County in California Bar Chart')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("arthritis_by_county_in_cali.png")
plt.show()

# Computing the average data value across all counties in California
avg_data_value = df['Data_Value'].mean()

# Sorting the counties in ascending order for the dropdown list
sorted_counties = sorted(df['LocationName'].unique())

# Interactive selection of county for visualization using ipywidgets
@widgets.interact(County=sorted_counties)
def plot_data(County):
    county_value = df[df['LocationName'] == County]['Data_Value'].values[0]

    labels = [County, 'Average across all counties in California']

    values = [county_value, avg_data_value]

    plt.figure(figsize=(8, 6))

    colors = ['blue', 'yellow']  # Changed bar colors to blue and yellow
    plt.bar(labels, values, color=colors)

    plt.ylabel('Data Value (Crude prevalence) - Percent')
    plt.title(f'Obesity Crude Prevalence in {County} vs Average Across all California Counties')
    plt.tight_layout()
    plt.show()

