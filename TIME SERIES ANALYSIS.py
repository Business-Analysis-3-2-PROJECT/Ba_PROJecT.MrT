
# =====================================================================
# PART C: TIME SERIES ANALYSIS (TSA) - Market Trend Visualization
# =====================================================================

print("\n--- Time Series Analysis: Market Trend Visualization (Final Fix) ---")
# Using 30 as an INTEGER window to bypass Pandas datetime index validation errors.
WINDOW_SIZE = 30 

# 1. Setup Data for TSA
df_tsa = df_full[['saledate', 'mmr']].copy()

# 2. Clean and prepare the data
df_tsa.dropna(subset=['saledate', 'mmr'], inplace=True)
df_tsa['saledate'] = pd.to_datetime(df_tsa['saledate'], errors='coerce') 
df_tsa.dropna(subset=['saledate'], inplace=True) 
df_tsa.sort_values('saledate', inplace=True)

# 3. Apply Integer Rolling Mean
# This is the final fix: Perform integer rolling on the numerical data after sorting by date.
df_tsa['rolling_mean_mmr'] = df_tsa['mmr'].rolling(window=WINDOW_SIZE).mean()

# 4. Plot the result
df_plot = df_tsa.dropna(subset=['rolling_mean_mmr'])

plt.figure(figsize=(12, 6))
plt.plot(df_plot['saledate'], df_plot['mmr'], label='Original MMR (Price Index)', alpha=0.5)
plt.plot(df_plot['saledate'], df_plot['rolling_mean_mmr'], label=f'{WINDOW_SIZE}-Day Rolling Mean (Market Trend)', color='red', linewidth=2)
plt.title('Time Series Analysis: MMR Market Trend Over Sale Dates')
plt.xlabel('Sale Date')
plt.ylabel('Manheim Market Report (MMR) Value')
plt.legend()
plt.grid(True)
plt.show()
