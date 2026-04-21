import airsim

client = airsim.MultirotorClient()
client.confirmConnection()

print("CONNECTED OK")