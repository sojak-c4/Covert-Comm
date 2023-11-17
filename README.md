
# Read Me Timing Based Covert Channel

## What It Does

This is a time based covert communication channel that transports morse code dots "." dashes "-" and spaces " ".

The sender inputs the receivers IP and port the receiver will be listening on. The sender will then input their plain text message and the message will get converted to morse code characters.

These morse characters are assigned three different time periods ("." = ~0.5s, "-" = ~3.s, " " = ~5s). When one of the characters is to be sent, the sender will wait before sending new a TCP packet for the time associated to the character.

The receivers code will measure the time and translate the delays back into morse charaters. The code will then translate the morse characters back into plain text and the receiver will get an output of the message on their terminal.

## How To Use

### To Generate An Executable

An ubuntu linux executable is included ("systemd_gui"), however, if you are running on a different system you will need to generate your own with Pyinstaller.

- To do this pip install pyinstaller
  - ($ pip install pyinstaller)
- Then use it to create an executable from the python code, must be in the same directory as python code,
  - ($ pyinstaller --onefile main.py -n <"optional blendy name">)
- The executable is saved in the ./dist folder

### To Use The Executable

Run the covert channel executable with either receiver or sender mode flags

- format: $ ./<"covert comm executable"> -m receive
- format: $ ./<"covert comm executable"> -m send

The receiver must be run first and when prompted input the ip of the machine they are listening on, an empty port that they want to listen on, and the timeout time in seconds for the socket to wait for that is greater than ten.

After the receiver is run, the sender can run the executable. They will be prompted to input the ip of the machine they are sending to, the port that the receiver will be listening on. And then a message that they want to send.

After the sender sends their message the receiver will start to receive TCP packets, the receiver must wait until the message is fully sent and they receive the output on their terminal. This may take a long time depending on the message length.

# Citations

Morse Code Function: GeeksToGeeks [https://www.geeksforgeeks.org/morse-code-translator-python/]()
