# F1 Telemetry Python Lab
# 

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastF1](https://img.shields.io/badge/FastF1-Telemetry-red)
![Data](https://img.shields.io/badge/Data-Analytics-green)
![Motorsport](https://img.shields.io/badge/Motorsport-F1-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

Professional telemetry analytics for Formula 1 using Python and FastF1.


Professional telemetry analytics for Formula 1 using Python and FastF1.

---

##  Features

- Qualifying lap analysis
- Sector time comparison
- Speed telemetry traces
- Terminal telemetry dashboard
- Driver lap comparison

Telemetry data from circuits such as the Shanghai International Circuit.

---

##  Tech Stack

- Python
- FastF1 telemetry API
- Pandas
- Matplotlib
- Rich terminal UI

---

##  Project Structure

src/
 +- f1_terminal.py
 +- f1_dashboard.py
 +- speed_compare.py
 +- sector_analysis.py
 +- f1_test.py

cache/
requirements.txt

---

##  Installation

Clone the repository:

git clone https://github.com/LauroBeck/f1-telemetry-python

Enter the project directory:

cd f1-telemetry-python

Create environment:

python -m venv f1-env

Activate environment (PowerShell):

.\f1-env\Scripts\Activate.ps1

Install dependencies:

pip install fastf1 pandas matplotlib rich

---

##  Run Telemetry Terminal

python src\f1_terminal.py

---

##  Example Analysis

The system compares telemetry between drivers and visualizes:

- speed vs track distance
- sector dominance
- fastest lap times

---

##  Teams Analyzed

Mercedes-AMG Petronas Formula One Team  
Scuderia Ferrari  
Oracle Red Bull Racing  
McLaren Formula 1 Team

---

##  Future Development

- tire degradation modeling
- lap delta visualization
- track map telemetry
- race strategy simulation
- AI lap prediction

---

##  Author

Lauro Beck

Financial analytics engineer and telemetry systems developer.

---

##  Project Goal

Build an open telemetry analytics platform similar to motorsport engineering dashboards.

