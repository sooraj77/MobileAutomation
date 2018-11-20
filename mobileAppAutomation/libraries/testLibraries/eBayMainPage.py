import time
import libraries.supportLibraries.baseMethods as base

#Page Methods
class EbayMainPage():
    def __init__(self,driver):
        self.driver = base.coreDriver(driver)
        self.locators = EbayMainPageLocators()
        self.longWait = 8
        self.keycodeEnter = 66

    def navigateToLoginScreen(self):
        """
        Method to navigate to Login Screen
        """
        try:
            navDrawer = self.driver.findElement(element = self.locators.btnNavigationDrawer, elementType = "id", timeout = "4")
            if not navDrawer:
                return False

            navDrawer.click()
            signIn = self.driver.findElement(element = self.locators.lblSignIn, elementType = "id", timeout = "4")
            if not signIn:
                return False

            signIn.click()
            return True
        except Exception as exp:
            print "Error in navigateToLoginScreen() : {}".format(exp)
            return False

    def searchItem(self,searchString):
        """
        Method to search for an item.
        args:
            searchString : String to search for
        """
        try:
            searchBox = self.driver.findElement(element = self.locators.lblSearchBox, elementType = "id", timeout = "4")
            if not searchBox:
                return False

            searchBox.click()
            searchField = self.driver.findElement(element = self.locators.lblSearchField, elementType = "id", timeout = "4")
            if not searchField:
                return False

            searchField.click()
            searchField.send_keys(searchString)
            self.driver.pressKey(self.keycodeEnter)
            time.sleep(self.longWait)
            return True 
        except Exception as exp:
            print "Error in navigateToLoginScreen() : {}".format(exp)
            return False

#Locators
class EbayMainPageLocators():
    
    def __init__(self):
        pass

    btnNavigationDrawer = "home"
    lblSignIn = "logo"
    lblSearchBox = "search_box"
    lblSearchField = "search_src_text"
