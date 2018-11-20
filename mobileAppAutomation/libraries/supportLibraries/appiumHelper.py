from subprocess import Popen, PIPE
import time


def startAppiumServer():
    try:
        print "Starting appium server..."
        appiumProc = Popen(['appium'], stdout=PIPE, stderr=PIPE)
        time.sleep(10)
        return appiumProc
    except Exception as exp:
        print "Error starting appium instance : {}".format(exp)
        return False
