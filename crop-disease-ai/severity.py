from sklearn.ensemble import RandomForestClassifier

X_train = [
    [95, 120], [90, 110], [85, 100],
    [70, 140], [65, 135], [60, 130],
    [40, 160], [35, 155], [30, 150],
    [10, 180], [15, 175], [20, 170],
]
y_train = [
    "High", "High", "High",
    "Medium", "Medium", "Medium",
    "Low", "Low", "Low",
    "None", "None", "None"
]

YIELD_LOSS = {
    "High":   "40-60%",
    "Medium": "15-30%",
    "Low":    "5-10%",
    "None":   "0%"
}

clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)

def estimate_severity(confidence, brightness=140):
    severity = clf.predict([[confidence, brightness]])[0]
    return {
        "severity": severity,
        "yield_loss": YIELD_LOSS[severity]
    }
