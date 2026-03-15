import fastf1
import pandas as pd

# Enable cache
fastf1.Cache.enable_cache('cache')

print("Loading F1 session telemetry...")

try:
    session = fastf1.get_session(2026, 'China', 'Q')
    session.load()

    laps = session.laps

    best_laps = laps[['Driver','LapTime']].sort_values('LapTime').head(10)

    print()
    print("Top 10 Qualifying Laps")
    print(best_laps)

except Exception as e:
    print("Telemetry loading error:")
    print(e)
