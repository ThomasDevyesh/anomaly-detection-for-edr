import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
@st.cache_data

def load_data():
    df = pd.read_csv("../data/all_files_combined_evtx_logs.csv")
    df['TimeCreated'] = pd.to_datetime(df['TimeCreated'], errors='coerce')
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("Anomaly Detection Settings")
model_choice = st.sidebar.selectbox("Choose Model", ["Isolation Forest", "LOF", "Autoencoder"])
top_k = st.sidebar.slider("Top-K Anomalies to Display", 10, 1000, 100)

# Define which column to use based on model
score_column = {
    "Isolation Forest": "AnomalyScore",
    "LOF": "LOF_Score",
    "Autoencoder": "AE_Error"
}[model_choice]

label_column = {
    "Isolation Forest": "IsAnomaly",
    "LOF": "LOF_Anomaly",
    "Autoencoder": "AE_Label"
}[model_choice]

# Gracefully handle missing model output
if score_column not in df.columns:
    st.warning(f"'{score_column}' not found in the dataset. Please run the {model_choice} model first to generate it.")
    st.stop()

# --- Main Dashboard ---
st.title("EDR Anomaly Detection Dashboard")

# Anomaly Score over Time
st.subheader(f"{model_choice} Anomaly Scores Over Time")
df_sorted = df.sort_values("TimeCreated")
plt.figure(figsize=(10, 4))
plt.plot(df_sorted["TimeCreated"], df_sorted[score_column], label=score_column, alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# Score Distribution
st.subheader(f"{model_choice} Score Distribution")
plt.figure(figsize=(8, 4))
sns.histplot(df[score_column], bins=50, kde=True, color="skyblue")
st.pyplot(plt)

# Show Top-K Anomalies
st.subheader(f"Top {top_k} Anomalies Detected by {model_choice}")
df_anomalies = df.sort_values(score_column, ascending=False).head(top_k)
st.dataframe(df_anomalies[["TimeCreated", "EventID", "Task", "Level", score_column]])

# Download Option
st.download_button("Download Anomalies as CSV",
                   data=df_anomalies.to_csv(index=False),
                   file_name="top_k_anomalies.csv",
                   mime="text/csv")
