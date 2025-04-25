from sklearn.ensemble import IsolationForest # type: ignore
from sklearn.neighbors import LocalOutlierFactor


def run_isolation_forest(X):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    scores = model.decision_function(X)
    labels = model.predict(X)
    return scores, labels

def run_lof(X, contamination=0.05):
    model = LocalOutlierFactor(n_neighbors=20, contamination=contamination)
    labels = model.fit_predict(X)
    # Inverse LOF score: lower score = more likely an outlier, so we flip it
    scores = -model.negative_outlier_factor_
    return scores, labels
