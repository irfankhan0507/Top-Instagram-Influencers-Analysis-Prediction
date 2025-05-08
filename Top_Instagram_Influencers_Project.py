import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a modern seaborn style
sns.set_style("whitegrid")

# Load your clean Excel dataset
df = pd.read_excel('top_instagram_influencers.xlsx')

# --------- SCATTER PLOT: Followers vs Engagement Rate ----------
plt.figure(figsize=(12, 8))
sns.scatterplot(
    x='followers', 
    y='60_day_eng_rate', 
    data=df,
    hue='country',  # Different colors for different countries
    palette='viridis', 
    s=150, 
    edgecolor='black'
)
plt.title('📈 Followers vs 60-Day Engagement Rate', fontsize=18, fontweight='bold')
plt.xlabel('Followers', fontsize=14)
plt.ylabel('60-Day Engagement Rate (%)', fontsize=14)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# --------- HISTOGRAM: Distribution of Influence Scores ----------
plt.figure(figsize=(12, 6))
sns.histplot(df['influence_score'], kde=True, color='skyblue', bins=10)
plt.title('📊 Distribution of Influence Scores', fontsize=18, fontweight='bold')
plt.xlabel('Influence Score', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# --------- BAR CHART: Top 10 Countries with Most Influencers ----------
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(12, 8))
sns.barplot(
    x=top_countries.values, 
    y=top_countries.index, 
    palette='magma'
)
plt.title('🌍 Top 10 Countries by Number of Influencers', fontsize=18, fontweight='bold')
plt.xlabel('Number of Influencers', fontsize=14)
plt.ylabel('Country', fontsize=14)

# Annotate bars with exact counts
for index, value in enumerate(top_countries.values):
    plt.text(value, index, str(value), color='black', ha='left', va='center', fontweight='bold')

plt.grid(axis='x')
plt.tight_layout()
plt.show()

# --------- FEATURE IMPORTANCE BAR CHART (if needed) ----------
# (This you can add after model training if you want!)

