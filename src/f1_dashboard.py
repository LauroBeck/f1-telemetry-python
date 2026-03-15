from rich.console import Console
from rich.table import Table
import fastf1

console = Console()

fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2026, 'China', 'Q')
session.load()

laps = session.laps[['Driver','LapTime']].sort_values('LapTime').head(10)

table = Table(title='F1 Qualifying Telemetry')

table.add_column('Driver')
table.add_column('LapTime')

for _, row in laps.iterrows():
    table.add_row(str(row['Driver']), str(row['LapTime']))

console.print(table)
