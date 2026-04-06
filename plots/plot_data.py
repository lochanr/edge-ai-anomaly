import matplotlib.pyplot as plt

temps = []
status = []

with open("data/data.csv", "r") as f:
    for line in f:
        t, s = line.strip().split(",")
        temps.append(int(t))
        status.append(s)

colors = ["red" if "Anomaly" in s else "green" for s in status]

plt.scatter(range(len(temps)), temps, c=colors)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Edge AI Anomaly Detection")

plt.show()
