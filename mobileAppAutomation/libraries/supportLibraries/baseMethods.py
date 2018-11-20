from appium import webdriver
import time


class coreDriver():
    """
    Implements core driver api's by wrapping core appium driver api's
    """
    def __init__(self, driver):
        self.driver = driver
        self.shortWait = 2

    def findElement(self, element, elementType, timeout = 5):
        """
        Abstraction method for core appium find_element* methods
        Implementing only those currently used. 
        """
        print "Looking for element : {0} with type : {1}".format(element,elementType)
        startTime =  time.time()
        while time.time() - startTime < timeout:
            try:
                if elementType == "id" or elementType == "resource-id":
                    el = self.driver.find_element_by_id(element)
                elif elementType == "class" or elementType == "class-name":
                    el = self.driver.find_element_by_class_name(element)
                return el
            except Exception as exp:
                print "Unable to locate element : {0} of type {1} : {2}. Retrying...".format(element,elementType,exp)
                time.sleep(self.shortWait)
        print "Failed to fine element {0} of type {1}".format(element,elementType)
        return False

    def pressKey(self,code):
        return self.driver.press_keycode(code)




