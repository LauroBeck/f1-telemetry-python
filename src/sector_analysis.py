import fastf1
import pandas as pd

fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2026, 'China', 'Q')
session.load()

laps = session.laps

sectors = laps[['Driver','Sector1Time','Sector2Time','Sector3Time']]

print()
print('Sector Performance')
print(sectors.sort_values('Sector1Time').head(10))
