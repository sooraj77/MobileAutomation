import time
import libraries.supportLibraries.baseMethods as base

#Page Methods
class EbayCheckOutPage():
    def __init__(self,driver):
        self.driver = base.coreDriver(driver)
        self.locators = EbayCheckOutPageLocators()

    def verifyCheckOutPage(self,itemTitle,itemPrice):
        """
        Method to verify if the checkout page item details matches details from search results page
        args:
            itemTitle: item title from search results screen
            itemPrice: item price from search resulsts screen

        """
        try:
            checkoutTitle = self.driver.findElement(element = self.locators.itemTitle, elementType = "id", timeout = "4")
            if not checkoutTitle:
                return False

            title = checkoutTitle.text
            if itemTitle != title:
                print "Item title does not match title in Search Results"
                titleStatus = False

            checkoutPrice = self.driver.findElement(element = self.locators.itemPrice, elementType = "id", timeout = "4")
            if not checkoutPrice:
                return False

            price = checkoutPrice.text
            if itemPrice != title:
                print "Item price does not match price in Search Results"
                priceStatus = False

            return titleStatus and priceStatus


        except Exception as exp:
            print "Error in verifyCheckOutPage() : {}".format(exp)
            return False

#Locators
class EbayCheckOutPageLocators():
    
    def __init__(self):
        pass

    itemTitle = "textview_item_name"
    itemPrice = "textview_item_price"

