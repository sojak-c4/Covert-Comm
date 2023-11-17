
# Read Me Timing Based Covert Channel

## What It Does

This is a time based covert communication channel that transports morse code dots "." dashes "-" and spaces " ".

The sender inputs the receivers IP and port the receiver will be listening on. The sender will then input their plain text message and the message will get converted to morse code characters.

These morse characters are assigned three different time periods ("." = ~0.5s, "-" = ~3.s, " " = ~5s). When one of the characters is to be sent, the sender will wait before sending new a TCP packet for the time associated to the character.

The receivers code will measure the time and translate the delays back into morse charaters. The code will then translate the morse characters back into plain text and the receiver will get an output of the message on their terminal.

## How To Use
### To Use as Python Code
1. Open 2 terminal instances. can both be on the same computer or on different computers on the same network. Terminal instances should be in the directory where the code is located.
2. On the receiving terminal run `python3 main.py -m receive`
3. Follow the prompts and type in the IP and port you are receiving on (e.g. 127.0.0.1:8080).
4. Enter a timeout time for how long the receiver will stay open and wait for a connection.
5. On the sender terminal run `python3 main.py -m send`
6. Type in the IP of the computer that you will be sending a message to (the receiver terminal's computer)
7. Type in your message when prompted and hit enter.
8. Wait for the message to fully finish on both terminals before closing the terminal. Partial messages are not possible. It is recommended to keep messages brief.

### To Generate An Executable

An ubuntu Linux executable is included ("systemd_gui"), however, if you are running on a different system you will need to generate your own with Pyinstaller.

- To do this pip install pyinstaller
  - ($ pip install pyinstaller)
- Then use it to create an executable from the python code, must be in the same directory as python code,
  - ($ pyinstaller --onefile main.py -n <"optional blendy name">)
- The executable is saved in the ./dist folder

#### To Use The Executable

Run the covert channel executable with either receiver or sender mode flags

- format: $ ./<"covert comm executable"> -m receive
- format: $ ./<"covert comm executable"> -m send

The receiver must be run first and when prompted input the ip of the machine they are listening on, an empty port that they want to listen on, and the timeout time in seconds for the socket to wait for that is greater than ten.

After the receiver is run, the sender can run the executable. They will be prompted to input the ip of the machine they are sending to, the port that the receiver will be listening on. And then a message that they want to send.

After the sender sends their message the receiver will start to receive TCP packets, the receiver must wait until the message is fully sent and they receive the output on their terminal. This may take a long time depending on the message length.

## Credits
Written as part of a 3-person group.

# Citations

Morse Code Function: GeeksToGeeks [https://www.geeksforgeeks.org/morse-code-translator-python/]()
