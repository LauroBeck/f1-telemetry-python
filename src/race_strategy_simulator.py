import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Race Strategy Simulator
# -----------------------------

year = 2023
gp = "Bahrain Grand Prix"
session_type = "R"

# Example tire degradation model (% lap time loss per lap)
tire_degradation = {
    "Soft": 0.25,   # seconds lost per lap
    "Medium": 0.15,
    "Hard": 0.10
}

# Example base lap times (seconds)
base_lap_times = {
    "Soft": 88.5,
    "Medium": 89.0,
    "Hard": 89.5
}

# Race settings
total_laps = 57
pit_strategy = [(15, "Medium"), (35, "Soft")]  # pit lap, new compound

# Initialize simulation
lap_times = []
current_tire = "Soft"
degradation = tire_degradation[current_tire]

for lap in range(1, total_laps + 1):
    lap_time = base_lap_times[current_tire] + degradation * lap
    # Pit stop check
    for pit_lap, new_tire in pit_strategy:
        if lap == pit_lap:
            lap_time += 22.0  # pit stop time
            current_tire = new_tire
            degradation = tire_degradation[current_tire]
    lap_times.append(lap_time)

laps = pd.DataFrame({
    "Lap": np.arange(1, total_laps + 1),
    "LapTime": lap_times
})

# Plot
plt.figure(figsize=(10,5))
plt.plot(laps["Lap"], laps["LapTime"], marker='o')
plt.title(f"Race Strategy Simulation: {gp}")
plt.xlabel("Lap")
plt.ylabel("Lap Time (s)")
plt.grid(True)
plt.show()
