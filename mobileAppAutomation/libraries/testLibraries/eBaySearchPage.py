import time
import random
import libraries.supportLibraries.baseMethods as base

#Page Methods
class EbaySearchPage():
    def __init__(self,driver):
        self.driver = base.coreDriver(driver)
        self.locators = EbaySearchLocators()
        self.longWait = 8

    def verifySearchResults(self):
        """
        Method to verify if the search results are displayed
        """
        try:
            resultCells = self.driver.findElement(element = self.locators.searchResultCell, elementType = "id", timeout = "4")
            if resultCells:
                return True
            else:
                return False

        except Exception as exp:
            print "Error in verifySearchResults() : {}".format(exp)
            return False       

    def selectRandomSearchResult(self):
        """
        Method to select a random search result from search results screen
        """
        try:
            resultCells = self.driver.findElement(element = self.locators.searchResultCell, elementType = "id", timeout = "4")
            if not resultCells:
                return False
            selectionCell = random.choice(resultCells)
            selectionPrice = selectionCell.find_element_by_id(self.locators.itemTitle)
            selectionTitle = selectionCell.find_element_by_id(self.locators.itemPrice)
            selectionCell.click()
            return selectionTitle,selectionPrice

        except Exception as exp:
            print "Error in selectRandomSearchResult() : {}".format(exp)
            return False

#Locators
class EbaySearchLocators():
    
    def __init__(self):
        pass

    searchResultCell = "cell_collection_item"
    itemTitle = "textview_item_title"
    itemPrice = "textview_item_price"

