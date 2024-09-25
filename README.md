OWI Maplin Robot (for Python 3)

This script has been forked from peterlavelle/maplinarm. It has been designed to work with Python 3 and also be more user friendly.

==============

Python script to control the Maplin USB robotic arm on your Raspberry PI.

Requirements
============

- Raspian
- Python 3
- pip
- pyusb Library

Installation
===========

Assumes you have not already installed from peterlavelle/maplinarm

If you have installed it already, only run the first, second and last bullet point steps.

- Install this repository by cloning it: <pre>git clone https://github.com/Cyclingbob/maplinarm maplinarm2</pre>
- change directory to this new folder: <pre>cd maplinarm2</pre>

- Create a new udev rules file at <pre>/etc/udev/rules.d/85-robotarm.rules</pre> with the contents
<pre>
SUBSYSTEM=="usb", ATTRS{idVendor}=="1267", ATTRS{idProduct}=="0000", ACTION=="add", GROUP="plugdev", MODE="0666"
</pre>
- Add your user to the plugdev group using the command: <pre>sudo usermod -aG plugdev yourusername</pre>
- Reboot the Pi with the command: <pre>sudo shutdown -r now</pre>
- Make the script executable with the command: <pre>chmod 755 main.py</pre>
- Install pip with the command: <pre>sudo apt-get install python-pip -y</pre>
- Install pyusb Library via pip with the command: <pre>sudo pip install pyusb</pre>
- Open the scripts and edit it to suit your needs (See Example Usage section for more info.)
- type <pre> python3 main.py </pre> to run. If you have problems running as a normal user, try running the script as root.

Moving the Arm
==============

Valid commands to send to the arm are:

The argument is the amount of time the script should wait from sending this instruction until continuing with the rest of the script.

- 'robot.moveBaseAntiClockwise()' - Rotates the base anti-clockwise
- 'robot.moveBaseClockwise()' - Rotates the base clockwise
- 'robot.shoulderUp() - Raises the shoulder
- 'robot.shoulderDown()' - Lowers the shoulder
- 'robot.elbowUp()' - Raises the elbow
- 'robot.elbowDown()' - Lowers the elbow
- 'robot.wristUp()' - Raises the wrist
- 'robot.wristDown()' - Lowers the wrist
- 'robot.gripOpen()' - Opens the grip
- 'robot.gripClose()' - Closes the grip
- 'robot.lightOn()' - Turns on the LED in the grip
- 'robot.lightOff()' - Turns the LED in the grip off
- 'robot.stop()' - Stops all movement of the arm
- 'robot.reconnect()' - Can be called if the USB connection fails.

Example Usage
=============

Find this code in `main.py`

<pre>
from maplinrobot import Robot
my_arm = Robot()
my_arm.moveBaseAntiClockwise()
</pre>

This will rotate the base of the arm clockwise for 1 second. Duration of each command is set by passing a float value 
to the `time` parameter like so: `my_arm.moveBaseAntiClockwise(2)`, for 2 seconds.

<pre>python3 main.py</pre>

The program may print out lots of debug output, this is due to print statements in <pre>maplinrobot.py</pre>