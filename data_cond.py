from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Step 1: Load JSON data
with open('./wx_pwrtest.json') as f:
    data = json.load(f)

# Step 2: Convert JSON to Pandas DataFrame
# Flatten weather and power data, considering the common structure between locations
def flatten_data(entry):
    flattened = pd.json_normalize(entry, 'weather').assign(location=entry['location'])
    power_data = pd.json_normalize(entry, 'power')
    for column in power_data.columns:
        flattened[column] = power_data.iloc[0][column]
    return flattened

df_list = [flatten_data(item) for item in data]
df = pd.concat(df_list, ignore_index=True)

for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert non-numeric columns that should be numeric
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Handling missing values by filling with the mean of the column
df.fillna(df.mean(), inplace=True)

# Step 3: Feature Engineering and Selection
# Assuming 'Load Watts' is the target variable and rest are features
X = df.drop(['Load Watts', 'location'], axis=1)  # Drop location or any non-numeric features if not encoded
y = df['Load Watts']

# Step 4: Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Model Training
#model = RandomForestRegressor(random_state=42)
model = HistGradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Step 6: Evaluation
mse = mean_squared_error(y_test, predictions)
print(f"Model MSE: {mse}")

# Note: Adjustments might be needed based on the specifics of your task, such as the choice of model,
# handling of categorical variables, and target variable selection.
