#!/usr/bin/env python3
import sys
import time
import os
import csv

# Add current directory to system path
sys.path.append(os.getcwd())

# Import the maplinrobot class
from maplinrobot import MaplinRobot

class RobotCommander():
    def __init__(self):
        self.csvfile = ''
        self.commands = ''

    def ParseArguments(self):
        try:
            if len(sys.argv) > 1:  # Valid number of arguments
                self.csvfile = str(sys.argv[1])
                return True
            else:
                return False
        except IndexError:
            print("None or wrong number of arguments supplied!\n")
            return False

    def CheckFileExists(self):
        if os.path.isfile(self.csvfile) and os.path.exists(self.csvfile):
            return True
        else:
            return False

    def ReadCSVFile(self):
        try:
            if self.ParseArguments() and self.CheckFileExists():
                with open(self.csvfile, newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    self.commands = list(reader)
                return True
            else:
                return False
        except csv.Error:
            print("Unable to load csv file\n")
            return False

    def RunCommands(self):
        try:
            r = MaplinRobot()
            if self.ReadCSVFile():
                for row in self.commands:
                    print(f"Running command '{str(row[0])}' for a duration of {float(row[1])} second(s) with a pause of {float(row[2])} second(s)")
                    if r.MoveArm(t=float(row[1]), cmd=str(row[0])):
                        time.sleep(float(row[2]))
                    else:
                        print("Problem sending commands. Exiting\n")
                        return False

                # All commands done. Stop the arm
                print("\nAll commands executed. Stopping the arm\n")
                r.StopArm()
                return True
            else:
                print("Something went wrong!\n")
                r.StopArm()
                return False

        except KeyboardInterrupt:
            print("Ctrl-C pressed. Exiting\n")
            return False

# Instantiate and run the robot commander
r = RobotCommander()
r.ParseArguments()
r.RunCommands()
