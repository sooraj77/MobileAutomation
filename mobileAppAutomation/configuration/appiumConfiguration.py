import runConfiguration
import os

#Appium Desired Capabilites

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desiredCaps = {}
desiredCaps['platformName'] = 'Android'
desiredCaps['platformVersion'] = '8.1.0'
desiredCaps['deviceName'] = 'Android Emulator'
desiredCaps['app'] = PATH(runConfiguration.applicationPath)