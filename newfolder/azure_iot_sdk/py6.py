import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
import time
import random
import string




async def main():
    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    await device_client.connect()

letters=5
async def Key_generator(letters):
    while True:
        str1=''.join(random.choices(string.ascii_letters+string.digits,k=letters))
        str2=''.join(random.choices(string.ascii_letters+string.digits,k=letters))
        str3=str1+str2
        print(str3)
        time.sleep(5)
        await device_client.send_message("This is a message that is being sent")
        print("Message successfully sent!")

        await device_client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())




