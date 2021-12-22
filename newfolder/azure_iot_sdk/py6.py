import random
import string
import time
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient


async def main():
    conn_str ="HostName=IoTServerTesting.azure-devices.net;DeviceId=training;SharedAccessKey=VMY8TQTg1zRqo8ey9vWLLgW8a7PzuSDobrPgtfH6Lew="

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    await device_client.connect()

    for i in range(50):
        str1 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        str2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        str3 = str1 + str2
        print("Sending message...",str3)
        time.sleep(2)
        await device_client.send_message("This is a message that is being sent")
        print("Message successfully sent!")

        await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())



