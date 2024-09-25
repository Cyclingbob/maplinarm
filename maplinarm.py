#!/usr/bin/env python3
import sys
import time
import os

sys.path.append(os.getcwd())

from maplinrobot import MaplinRobot

class Robot():
    def __init__(self):
        self._robot = None
        self.reconnect()
    
    def reconnect(self):
        self._robot = MaplinRobot()
    
    def moveBaseAntiClockwise(self, time):
        return self._robot.MoveArm(time, "base-anti-clockwise")

    def moveBaseClockwise(self, time):
        return self._robot.MoveArm(time, "base-clockwise")

    def shoulderUp(self, time):
        return self._robot.MoveArm(time, "shoulder-up")

    def shoulderDown(self, time):
        return self._robot.MoveArm(time, "shoulder-down")
    
    def elbowUp(self, time):
        return self._robot.MoveArm(time, "elbow-up")

    def elbowDown(self, time):
        return self._robot.MoveArm(time, "elbow-down")

    def wristUp(self, time):
        return self._robot.MoveArm(time, "wrist-up")

    def wristDown(self, time):
        return self._robot.MoveArm(time, "wrist-down")

    def gripOpen(self, time):
        return self._robot.MoveArm(time, "grip-open")

    def gripClose(self, time):
        return self._robot.MoveArm(time, "grip-close")

    def lightOn(self, time):
        return self._robot.MoveArm(time, "light-on")

    def lightOff(self, time):
        return self._robot.MoveArm(time, "light-off")

    def stop(self, time):
        return self._robot.MoveArm(time, "stop")
