import os
import asyncio
from six.moves import input
import threading
from azure.iot.device.aio import IoTHubDeviceClient


async def main():

    conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)


    await device_client.connect()


    def message_received_handler(message):
        print("the data in the message received was ")
        print(message.data)
        print("custom properties are")
        print(message.custom_properties)
        print("content Type: {0}".format(message.content_type))
        print("")

    device_client.on_message_received = message_received_handler


    def stdin_listener():
        while True:
            selection = input("Press Q to quit\n")
            if selection == "Q" or selection == "q":
                print("Quitting...")
                break


    loop = asyncio.get_running_loop()
    user_finished = loop.run_in_executor(None, stdin_listener)


    await user_finished

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())