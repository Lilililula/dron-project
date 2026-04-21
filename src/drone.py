import airsim
import time
import random

client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True)
client.armDisarm(True)

print("Взлёт...")
client.takeoffAsync().join()

client.moveToZAsync(-30, 5).join()

print("Хаотичный маршрут...")

start = time.time()

while time.time() - start < 60:
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    z = random.uniform(-20, -40)
    speed = random.uniform(5, 10)

    print(f"Точка: x={x:.1f}, y={y:.1f}, z={z:.1f}")

    client.moveToPositionAsync(x, y, z, speed).join()

print("Посадка...")
client.landAsync().join()

client.armDisarm(False)
client.enableApiControl(False)

print("Готово")
