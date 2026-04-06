# Edge AI Anomaly Detection System

This project demonstrates a simple edge-based anomaly detection system using both rule-based logic and machine learning.

## Features
- Simulated sensor data
- Threshold-based anomaly detection
- ML-based anomaly detection (Isolation Forest)
- Hybrid decision system
- Data logging and visualization

## Architecture
Sensor → Processing → Hybrid Decision → Logging → Visualization

## Tech Stack
- Python
- scikit-learn
- matplotlib

## How to Run

```bash
pip install -r requirements.txt
python src/train_model.py
python src/hybrid_system.py
python plots/plot_data.py
'''

