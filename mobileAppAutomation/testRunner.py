#Standard Imports
from appium import webdriver
import collections
import importlib
import datetime
import unittest
import inspect
import time
import sys
import os

#Framework Imports
import libraries.supportLibraries.reportGenerator as reporter
import libraries.supportLibraries.appiumHelper as appiumHelper
import configuration.appiumConfiguration as appiumConfiguration

#
#Function to get the tests from executionManager file where tests to be run are stored
#
def getTests():
    try:
        validEntries = []

        if os.path.exists(os.path.abspath(testConfigPath)):
            configFile = open(os.path.abspath(testConfigPath),'rb').read()
            configFile = configFile.split("\n")
            entries = [entry for entry in configFile if not entry.startswith('#')]
            validEntries = [entry for entry in entries if entry and os.path.exists(os.path.abspath(entry))]

        if not validEntries:
            print "No valid test entries found in {}!".format(testConfigPath)
        else:
            print "Testcases for execution are as follows: {0}".format('\n'.join(validEntries))
    
        return validEntries

    except Exception as exp:
        print "Error in parsing executionManager file: {}".format(exp)
        return []

#
#Function to setup the test env
#
def envSetup():
    try:
        #Create test results folder
        global executionFolder
        if not os.path.exists('testResults'):
            os.mkdir('testResults')

        executionTimestamp = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        executionFolder = os.path.join('testResults','executionResult_' + executionTimestamp)
        os.mkdir(executionFolder)
        
        #Start Appium Server Instance
        global appiumProcess
        global driver
        appiumProcess = appiumHelper.startAppiumServer()
        print "Initializing Appium Instance..."
        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', appiumConfiguration.desiredCaps)
        time.sleep(8)
        if not appiumProcess:
            return False

        return True
    except Exception as exp:
        print "Error in envSetup() : {}".format(exp)
        return False

#
#Function to clean up the Env
#
def cleanUp():
    try:
       global appiumProcess
       appiumProcess.terminate()
    except Exception as exp:
        print "Error in Clean Up function: {}".format(exp)


if __name__ == "__main__":
    #Adding current working directory to PATH for imports
    sys.path.append(os.path.abspath(os.getcwd()))
    executionFolder = None
    appiumProcess = None
    driver = None

    #Path to test execution configurations
    testConfigPath = './configuration/executionManager.config'

    if not envSetup():
        cleanUp()
        print "Error Setting up Env, Exiting!"
        sys.exit(1)

    tests = getTests()

    testResults = collections.OrderedDict([])
    for testEntry in tests:
        importedTest = importlib.import_module(testEntry[:-3].replace('/','.'))
        testClassObject = inspect.getmembers(importedTest, inspect.isclass)[0][1]

        testClass = unittest.TestLoader().loadTestsFromTestCase(testClassObject)

        #Setting the path for screenshot capture
        for items in testClass:
            items.executionFolderPath = executionFolder
            items.driver = driver

        unittest.TextTestRunner(verbosity=3).run(testClass)

        for test in testClass:
            if hasattr(test,'testResults'):
                testResults.update(test.testResults)
            
        jsonFile = os.path.join(executionFolder,'testReport.JSON')
        jsonreportStatus = reporter.generateJSONReport(jsonFile,testResults)
        if not jsonreportStatus:
            print "JSON report generation failed..."
        else:
            print "JSON report generation successful..."

        reportHTMLFile = os.path.join(executionFolder,'testReport.html')
        htmlReportStatus = reporter.generateReportHTML(reportHTMLFile,testResults)
        if not htmlReportStatus:
            print "HTML report generation failed..."
        else:
            print "HTML report generation successful..."

    cleanUp()
