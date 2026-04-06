import random
import time
import pickle

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

print("Hybrid system running...\n")

with open("data/data.csv", "a") as f:
    while True:
        temp = random.randint(20, 100)

        if temp > 85:
            status = "Anomaly (Threshold)"
        elif temp < 75:
            status = "Normal (Threshold)"
        else:
            prediction = model.predict([[temp]])[0]
            status = "Anomaly (ML)" if prediction == -1 else "Normal (ML)"

        print(f"Temp: {temp}, Status: {status}")
        f.write(f"{temp},{status}\n")
        f.flush()

        time.sleep(2)
