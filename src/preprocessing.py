import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df['TimeCreated'] = pd.to_datetime(df['TimeCreated'], errors='coerce')
    df = df.dropna(subset=['EventID', 'TimeCreated'])
    return df

def extract_features(df):
    df['Hour'] = df['TimeCreated'].dt.hour
    df['DayOfWeek'] = df['TimeCreated'].dt.dayofweek
    return df[['EventID', 'Task', 'Level', 'Hour', 'DayOfWeek']]
