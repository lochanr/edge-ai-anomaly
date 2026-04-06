import pickle
from sklearn.ensemble import IsolationForest
import random

data = [[random.randint(20, 70)] for _ in range(200)]

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved.")
