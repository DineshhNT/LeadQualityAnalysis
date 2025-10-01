import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import matplotlib.dates as mdates

# Load the Excel dataset
df = pd.read_excel("Analyst case study dataset 1.xls")

# Preview the dataset
print(df.head())
print(df.columns)

# Define lead quality scoring function
good_status = ["Closed", "EP Sent", "EP Received", "EP Confirmed"]
bad_status = ["Unable to Contact", "Contacted - Invalid Profile", "Contacted - Doesn't Qualify"]

def quality_score(status):
    if status == "Closed":
        return 10
    elif status in ["EP Confirmed", "EP Received", "EP Sent"]:
        return 8
    elif status in bad_status:
        return 2
    elif status == "Unknown":
        return 5
    else:
        return 5

# Apply quality score to DataFrame
df["QualityScore"] = df["CallStatus"].apply(quality_score)

# Convert LeadCreated to datetime
df['LeadCreated'] = pd.to_datetime(df['LeadCreated'])

# --- 1. Lead Quality Over Time ---

# Group by Year-Month period; calculate average quality score
quality_by_month = df.groupby(df['LeadCreated'].dt.to_period('M'))['QualityScore'].mean().reset_index()
# Convert period to timestamp for plotting
quality_by_month['LeadCreated'] = quality_by_month['LeadCreated'].dt.to_timestamp()

# Plot average lead quality over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=quality_by_month, x='LeadCreated', y='QualityScore', marker='o')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.title("Average Lead Quality Score Over Time")
plt.xlabel("Month")
plt.ylabel("Average Quality Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("lead_quality_over_time.png")
plt.close()

# Trend significance with linear regression
months_numeric = np.arange(len(quality_by_month))
result = linregress(months_numeric, quality_by_month['QualityScore'])
print('\nTrend Slope:', result.slope, 'p-value:', result.pvalue)

# --- 2. Segment Analysis ---

segments = ['WidgetName', 'PublisherZoneName', 'PublisherCampaignName', 'AdvertiserCampaignName', 'State', 'Partner']
segment_stats = {}

for seg in segments:
    temp = df.groupby(seg)['QualityScore'].agg(['mean', 'count']).sort_values('mean', ascending=False)
    segment_stats[seg] = temp
    print(f"\n--- {seg} Top 5 ---")
    print(temp.head())

    # Plot top 10 segment average quality
    plt.figure(figsize=(14, 6))
    sns.barplot(data=temp.head(10).reset_index(), x=seg, y='mean')
    plt.xticks(rotation=45)
    plt.title(f"Top 10 {seg} by Average Quality")
    plt.tight_layout()
    plt.savefig(f"quality_by_{seg.lower()}.png")
    plt.close()

# --- 3. Boosting Lead Quality ---

best_widgets = segment_stats['WidgetName'].head(3).index.tolist()
print("\nBest performing widgets for high quality:", best_widgets)

top_widget_df = df[df['WidgetName'].isin(best_widgets)]
new_mean = top_widget_df['QualityScore'].mean()
print("Estimated average lead quality if only top widgets are used:", new_mean)

# Pie chart for widget lead count distribution
widget_counts = df['WidgetName'].value_counts().head(10)
plt.figure(figsize=(8, 8))
plt.pie(widget_counts, labels=widget_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 10 Widgets by Lead Count Distribution")
plt.tight_layout()
plt.savefig("widget_count_distribution.png")
plt.close()

# Save analyzed data for report or further use
df.to_csv("analyzed_leads.csv", index=False)

print("Analysis complete. Outputs saved to CSV and PNG files.")
