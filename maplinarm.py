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
    
    def moveBaseAntiClockwise(self, time=1):
        return self._robot.MoveArm(time=1, "base-anti-clockwise")

    def moveBaseClockwise(self, time=1):
        return self._robot.MoveArm(time, "base-clockwise")

    def shoulderUp(self, time=1):
        return self._robot.MoveArm(time, "shoulder-up")

    def shoulderDown(self, time=1):
        return self._robot.MoveArm(time, "shoulder-down")
    
    def elbowUp(self, time=1):
        return self._robot.MoveArm(time, "elbow-up")

    def elbowDown(self, time=1):
        return self._robot.MoveArm(time, "elbow-down")

    def wristUp(self, time=1):
        return self._robot.MoveArm(time, "wrist-up")

    def wristDown(self, time=1):
        return self._robot.MoveArm(time, "wrist-down")

    def gripOpen(self, time=1):
        return self._robot.MoveArm(time, "grip-open")

    def gripClose(self, time=1):
        return self._robot.MoveArm(time, "grip-close")

    def lightOn(self, time=1):
        return self._robot.MoveArm(time, "light-on")

    def lightOff(self, time=1):
        return self._robot.MoveArm(time, "light-off")

    def stop(self, time=1):
        return self._robot.MoveArm(time, "stop")
