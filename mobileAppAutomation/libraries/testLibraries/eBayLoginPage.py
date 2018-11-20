import time
import libraries.supportLibraries.baseMethods as base

#Page Methods
class EbayLoginPage():
    def __init__(self,driver):
        self.driver = base.coreDriver(driver)
        self.locators = EbayLoginPageLocators()
        self.waitLong = 8
        self.waitShort = 2

    def login(self,username,password):
        """
        Method to login to eBay app
        args:
            username: username to use for login
            password: password to use for login
        """
        try:
            userNameField = self.driver.findElement(element = self.locators.lblUsernameField, elementType = "id", timeout = "4")
            if not userNameField:
                return False

            userNameField.click()
            userNameField.send_keys(username)
            time.sleep(self.waitShort)
            passwordField = self.driver.findElement(element = self.locators.lblPasswordField, elementType = "id", timeout = "4")
            if not passwordField:
                return False

            passwordField.click()
            passwordField.send_keys(password)
            time.sleep(self.waitShort)

            signIn = self.driver.findElement(element = self.locators.signIn, elementType = "id", timeout = "4")
            if not signIn:
                return False

            signIn.click()
            time.sleep(self.waitLong)
            #handler for No Thanks pop-up
            noThanks = self.driver.findElement(element = self.locators.btnNoThanks, elementType = "id", timeout = "4")
            if noThanks:
                noThanks.click()
            return True
        except Exception as exp:
            print "Error in login(): {}".format(exp)
            return False
        return True


#Locators
class EbayLoginPageLocators():
    
    def __init__(self):
        pass

    lblUsernameField = "edit_text_username"
    lblPasswordField = "edit_text_password"
    btnNoThanks = "button_google_deny"
    signIn = "button_sign_in"
