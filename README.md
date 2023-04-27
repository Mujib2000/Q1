# Q1
Publish PC battery status over BLE (Bluetooth Low Energy)

This project provides a Python script that may be used to create a BLE Peripheral that transmits the battery level of a computer over BLE.

Prerequisites
The following is necessary before running this script:

A BLE radio on your computer -A PC with Python 3.8 or later installed -The 'bluepy' library installed on your computer (pip can be used to do this: 'pip install bluepy').

Application of the Script
The following are the steps to run the script:

1) Save this repository to your PC in a copy.
2) Open a terminal or command prompt on your local computer.
3) Visit the cloned directory for the repository.
4) To start the script, carry out the subsequent command.
    
    " python code.py "

5) Every 200 milliseconds, the script will begin promoting the "PC Battery" BLE peripheral. Once a device is connected to a peripheral, it will display a feature that displays the battery level.
6) You can connect to the "PC Battery" Peripheral and search for nearby BLE devices using the NRF CONNECT Mobile App (available for both Android and iOS).
7) After connecting, you may check the PC's current battery level by reading the battery level characteristic. Both notify and read operations are supported by the characteristic.

Troubleshooting

Try the following if you experience any problems running the script:

-Confirm that the BLE radio on your computer is activated and discoverable.
-Confirm that pip was used to install the Bluepy library.
-Try restarting the script or the BLE radio on your PC.

Please refer to the Bluepy library documentation or file a bug report on this repository if you keep running into problems.
