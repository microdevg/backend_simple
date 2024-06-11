import servicios.mqtt as mqtt


if __name__ == "__main__":


    client = mqtt.get_client()

    client.loop_forever()
    while True:
        pass
