import socket
import time
import random


# Function to send the morse code to the receiver
def send_data(data, host, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the host and port
    server_address = (host, int(port))
    sock.connect(server_address)

    dummy_msg = str(random.randbytes(random.randint(1, 128)))[2:].replace(
        "\\", ""
    )  # randomized junk data for varying length
    sock.sendall(dummy_msg.encode("utf-8"))  # first message to start counter

    # For loop sends all data
    for i in range(len(data)):
        dummy_msg = str(random.randbytes(random.randint(1, 128)))[2:].replace(
            "\\", ""
        )  # randomized junk data for varying length

        if data[i] == ".":
            time.sleep(0.50)  # putting in small delay for dot to prevent misses
            try:
                # Send data
                sock.sendall(
                    dummy_msg.encode("utf-8")
                )  # encode() converts string to bytes to send
                print("sent: .")
            except Exception as e:
                print("ERROR: Your . sending didn't work :(", e)
        elif data[i] == "-":
            time.sleep(2.9)     # Delay for dash
            try:
                sock.sendall(dummy_msg.encode("utf-8"))
                print("sent: -")
            except Exception as e:
                print("ERROR: Your - sending didn't work :(", e)
        elif data[i] == " ":
            time.sleep(5.3)     # Delay for space
            try:
                sock.sendall(dummy_msg.encode("utf-8"))
                print("sent: -space-")
            except Exception as e:
                print("ERROR: Your -space- sending didn't work :(", e)
        else:
            print("Something went wrong")

    time.sleep(7.7)  # Time for receiver to recognize socket close
    sock.sendall(dummy_msg.encode("utf-8"))
    sock.close()
    print("Closed Socket Comms Ended")
