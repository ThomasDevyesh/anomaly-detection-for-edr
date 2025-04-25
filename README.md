# AI-Based Anomaly Detection in Endpoint Logs (EDR Integration)

This project investigates the use of machine learning models to detect anomalies in endpoint logs (e.g., Windows Event Logs / Sysmon) as a foundation for enhancing adaptive deception within EDR systems.

---

## 🚀 Project Highlights

- Uses real Windows `.evtx` logs from publicly available APT/malware simulations
- Applies multiple unsupervised anomaly detection models:
  - Isolation Forest
  - Local Outlier Factor (LOF)
  - Standard Autoencoder (AE)
- Compares model outputs using score distributions, overlaps, and visual analysis
- Includes an interactive **Streamlit dashboard** to explore anomalies

---

## 🧪 Folder Structure
```
anomaly-detection-edr-project/
├── data/
│   └── all_files_combined_evtx_logs.csv        # Final processed data
├── notebooks/
│   └── 01_exploration.ipynb                    # Where you trained models + saved scores
├── src/
│   ├── preprocessing.py                        # load_and_clean(), extract_features()
│   ├── models.py                               # IF, LOF
│   └── autoencoder.py                          # Autoencoder
├── app/
│   └── streamlit_dashboard.py                  # Streamlit dashboard app
├── README.md                                   # Project description + usage
├── requirements.txt                            # Required Python packages
└── .gitignore                                  # Ignore __pycache__/, .DS_Store, etc.
```

## For Dr. Abdul Shahid (Professor for AI/ML in Cybersecurity)
All outputs, visuals, and core models are included in:
- notebooks/01_exploration.ipynb
- app/streamlit_dashboard.py

To view dashboard, please install necessary python modules using `requirements.txt` and launch streamlit using the command `streamlit run app/streamlit_dashboard.py`

## 📈 Dashboard Features
- View anomaly scores by model (IF, LOF, AE)
- Top-k anomalies table with filtering
- Download flagged anomalies as CSV

## 📓 Train Models & Visualize

Run `notebooks/01_exploration.ipynb` <br>
**Note: Make sure to execute the last block i.e. `df.to_csv...`**

Launch Dashboard using the command `streamlit run app/streamlit_dashboard.py`

## 📚 Acknowledgements
EVTX samples from [sbousseaden - EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES)


