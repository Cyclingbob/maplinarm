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

- Install this repository by cloning it: <strong>git clone https://github.com/Cyclingbob/maplinarm maplinarm2</strong>
- change directory to this new folder: <strong>cd maplinarm2</strong>

- Create a new udev rules file at <strong>/etc/udev/rules.d/85-robotarm.rules</strong> with the contents
<pre>
SUBSYSTEM=="usb", ATTRS{idVendor}=="1267", ATTRS{idProduct}=="0000", ACTION=="add", GROUP="plugdev", MODE="0666"
</pre>
- Add your user to the plugdev group using the command: <pre>sudo usermod -aG plugdev yourusername</pre>
- Reboot the Pi with the command: <pre>sudo shutdown -r now</pre>
- Make the script executable with the command: <pre>chmod 755 main.py</pre>
- Install pip with the command: <pre>sudo apt-get install python-pip -y</pre>
- Install pyusb Library via pip with the command: <pre>sudo pip install pyusb</pre>
- Open the scripts and edit it to suit your needs (See Example Usage section for more info.)
- type <strong> python3 main.py </strong> to run. If you have problems running as a normal user, try running the script as root.

Moving the Arm
==============

Valid commands to send to the arm are:

The argument is the amount of time the script should wait from sending this instruction until continuing with the rest of the script.

- 'robot.moveBaseAntiClockwise(1)' - Rotates the base anti-clockwise
- 'robot.moveBaseClockwise(1)' - Rotates the base clockwise
- 'robot.shoulderUp(1) - Raises the shoulder
- 'robot.shoulderDown(1)' - Lowers the shoulder
- 'robot.elbowUp(1)' - Raises the elbow
- 'robot.elbowDown(1)' - Lowers the elbow
- 'robot.wristUp(1)' - Raises the wrist
- 'robot.wristDown(1)' - Lowers the wrist
- 'robot.gripOpen(1)' - Opens the grip
- 'robot.gripClose(1)' - Closes the grip
- 'robot.lightOn(1)' - Turns on the LED in the grip
- 'robot.lightOff(1)' - Turns the LED in the grip off
- 'robot.stop(1)' - Stops all movement of the arm
- 'robot.reconnect()' - Can be called if the USB connection fails.

Example Usage
=============

Find this code in <pre>main.py</pre>

<pre>
from maplinrobot import Robot
my_arm = Robot()
my_arm.moveBaseAntiClockwise(1)
</pre>

This will rotate the base of the arm clockwise for 1 second. Duration of each command is set by passing a float value 
to the <strong>time</strong> parameter.

<pre>python3 main.py</pre>

The program may print out lots of debug output, this is due to print statements in <pre>maplinrobot.py</pre>.