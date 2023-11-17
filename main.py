import receiver
import sender
import argparse
import morse_code_translator


def main():
    print("hello world")

    parser = argparse.ArgumentParser(description="Welcome to Xx_C0V3RT-C0MZZ_xX!")
    parser.add_argument(
        "-m", "--mode", type=str, help='Select mode: "send" or "receive".'
    )

    args = parser.parse_args()

    if args.mode == "send":  # Sender Mode
        print("\nSender Mode Activated!")
        receiverIpAndPort = input(
            'Input the IP and Port of the receiver (e.g. format: "127.0.0.1:8080"): '
        )
        try:
            ip, port = receiverIpAndPort.split(":")
        except:
            print("Error with IP and Port input, ensure format is correct.")

        plainTextMsg = input("Input the message to send: ")

        myMorseMsg = morse_code_translator.encrypt(plainTextMsg)

        print("\nSending message: ", myMorseMsg)
        sender.send_data(myMorseMsg, ip, port)

        print("\nMessage has been sent. Goodbye :)")

    # Receiver mode
    elif args.mode == "receive":
        print("\nReceiver Mode Activated!")

        receiverIpAndPort = input(
            'Input the public IP of your machine and Port to receive on (e.g. format: "127.0.0.1:8080"): '
        )
        try:
            ip, port = receiverIpAndPort.split(":")
        except:
            print("Error with IP and Port input, ensure format is correct.")
        timeOutSecs = input("Input custom timeout time (in seconds): ")
        receivedMorseMsg = receiver.receive_on_port(
            str(ip), int(port), float(timeOutSecs)
        )
        receivedPlainMsg = morse_code_translator.decrypt(receivedMorseMsg)
        print("Message Received:\n", receivedPlainMsg)

    else:
        print('ERROR: no mode arg found, try adding "-m send" or "-m receive"')


# Executes the main function
if __name__ == "__main__":
    main()
