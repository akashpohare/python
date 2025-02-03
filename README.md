
import asyncio
import websockets
import json
import ssl

# Qlik Sense Server details
qlik_sense_server = "wss://your-qlik-sense-server.com/app/<app-id>"

# Path to your client certificate and key files
cert_file = "path/to/your/client.crt"
key_file = "path/to/your/client.key"

# Create an SSL context with client certificates
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)

async def connect_to_qlik_sense():
    async with websockets.connect(
        qlik_sense_server,
        ssl=ssl_context,  # Pass the SSL context with client certificates
    ) as websocket:
        print("Connected to Qlik Sense Engine API using client certificates")

        # Send a message to the Qlik Sense Engine API
        message = {
            "method": "GetDocList",
            "handle": -1,
            "params": [],
            "outKey": -1,
            "id": 1
        }
        await websocket.send(json.dumps(message))
        print("Sent message to Qlik Sense Engine API")

        # Receive a response from the Qlik Sense Engine API
        response = await websocket.recv()
        print("Received response from Qlik Sense Engine API:")
        print(json.loads(response))

# Run the WebSocket connection
asyncio.get_event_loop().run_until_complete(connect_to_qlik_sense())
