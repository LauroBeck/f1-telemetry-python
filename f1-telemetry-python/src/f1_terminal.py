import fastf1
import pandas as pd
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
import logging

# Reduce FastF1 logs
logging.getLogger('fastf1').setLevel(logging.ERROR)

console = Console()

fastf1.Cache.enable_cache('cache')

console.print("[bold green]F1 TELEMETRY TERMINAL[/bold green]")
console.print("Loading telemetry session...\n")

session = fastf1.get_session(2026, 'China', 'Q')
session.load()

laps = session.laps

# -----------------------------
# Top Lap Times
# -----------------------------
best_laps = laps[['Driver','LapTime']].sort_values('LapTime').head(10)

table = Table(title="Top Qualifying Laps")

table.add_column("Driver")
table.add_column("LapTime")

for _, row in best_laps.iterrows():
    table.add_row(str(row['Driver']), str(row['LapTime']))

console.print(table)

# -----------------------------
# Sector Analysis
# -----------------------------
console.print("\n[bold cyan]Sector Performance[/bold cyan]")

sectors = laps[['Driver','Sector1Time','Sector2Time','Sector3Time']]
print(sectors.sort_values('Sector1Time').head(10))

# -----------------------------
# Speed Telemetry Comparison
# -----------------------------
console.print("\nGenerating telemetry speed comparison...")

driver1 = 'HAM'
driver2 = 'VER'

lap1 = laps.pick_driver(driver1).pick_fastest()
lap2 = laps.pick_driver(driver2).pick_fastest()

tel1 = lap1.get_car_data().add_distance()
tel2 = lap2.get_car_data().add_distance()

plt.figure()

plt.plot(tel1['Distance'], tel1['Speed'], label=driver1)
plt.plot(tel2['Distance'], tel2['Speed'], label=driver2)

plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("Speed Trace Comparison")
plt.legend()

plt.show()
