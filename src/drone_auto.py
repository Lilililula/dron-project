import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True)
client.armDisarm(True)

print("Взлёт...")
client.takeoffAsync().join()

time.sleep(2)

print("Вперёд...")
client.moveByVelocityAsync(2, 0, 0, 3).join()

time.sleep(2)

print("Посадка...")
client.landAsync().join()

client.armDisarm(False)
client.enableApiControl(False)

print("Готово")