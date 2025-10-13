# --- 2. Data Loading and Setup (WITH SAMPLING) ---
file_path = '../data/car_prices.csv'
SAMPLE_SIZE = 50000
MIN_SAMPLES = 1000
try:
 df_full = pd.read_csv(file_path)

 # *** FIX: Reduce data size using random sampling ***
 if df_full.shape[0] > SAMPLE_SIZE:
 df = df_full.sample(n=SAMPLE_SIZE, random_state=42)
 print(f"Dataset '{file_path}' loaded successfully. Sampled down to
{df.shape[0]} rows.")
 else:
 df = df_full
 print(f"Dataset '{file_path}' loaded successfully. Shape:
{df.shape}")

 if df.shape[0] < MIN_SAMPLES:
 print(f"Warning: Dataset size {df.shape[0]} is too small for
proper ML/DL training.")
except FileNotFoundError:
 print(f"Error: File not found at {file_path}. Using dummy data for
demonstration.")
 data = {
 'year': [2015, 2017, 2016, 2018, 2014, 2019, 2015, 2017]