import fastf1
import matplotlib.pyplot as plt

# Enable telemetry cache
fastf1.Cache.enable_cache('cache')

print("Loading session telemetry...")

session = fastf1.get_session(2026, 'China', 'Q')
session.load()

# Select two drivers
driver1 = 'HAM'
driver2 = 'VER'

laps = session.laps

lap1 = laps.pick_driver(driver1).pick_fastest()
lap2 = laps.pick_driver(driver2).pick_fastest()

tel1 = lap1.get_car_data().add_distance()
tel2 = lap2.get_car_data().add_distance()

plt.figure()

plt.plot(tel1['Distance'], tel1['Speed'], label=driver1)
plt.plot(tel2['Distance'], tel2['Speed'], label=driver2)

plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.title('Speed Trace Comparison')
plt.legend()

plt.show()
