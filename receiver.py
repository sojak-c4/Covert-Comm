import socket
import select
import time


def receive_on_port(myIp, port, timeout_seconds):
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )  # PRODUCTION VERSION
    server_socket.bind((myIp, port))
    server_socket.listen(1)
    morseString = ""

    print(f"Listening for incoming messages on port {port}...")

    # Set the server socket as the socket to watch for incoming data
    inputs = [server_socket]

    while True:
        # Use select to wait for incoming data or a timeout
        readable, _, _ = select.select(inputs, [], [], timeout_seconds)

        if not readable:
            # Timeout reached, exit the loop
            print(f"Timeout: No data received within {timeout_seconds} seconds.")
            break

        # Accept the incoming connection
        connection, addr = server_socket.accept()

        print(f"Connection established with {addr}")

        timestamp = 0
        old_timestamp = 0
        time_difference = 0
        try:
            # Receive the packets 
            while time_difference <= 10:
                data = connection.recv(1024).decode()
                timestamp = time.time()

                if old_timestamp != 0:
                    time_difference = timestamp - old_timestamp     # calculate time since last message

                    # Analyze time differences and translate to morse
                    if time_difference < 1.7:
                        morseString += "."
                        print("Received: .")
                    elif 1.7 <= time_difference < 4.1:
                        morseString += "-"
                        print("Received: -")
                    elif 4.1 <= time_difference < 6.5:
                        morseString += " "
                        print("Received: -space- ")
                    elif 6.5 <= time_difference:
                        print("Ending!")
                        break
                    else:
                        print("ERROR HIT ELSE STATEMENT")
                old_timestamp = timestamp   # Update the time used for comparison

        except Exception as e:
            print("ERROR: Something went wrong with receiver", e)

        connection.close()  # Close connection when we are done

        print("Morse String: ", morseString)
        return morseString
