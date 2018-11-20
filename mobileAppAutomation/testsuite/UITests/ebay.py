import unittest

from libraries.supportLibraries.testWrapper import wrapped_test
import libraries.supportLibraries.common as common
import testConstants

from libraries.testLibraries import eBayMainPage
from libraries.testLibraries import eBayLoginPage
from libraries.testLibraries import eBaySearchPage
from libraries.testLibraries import eBayCheckOutPage


class Ebay(unittest.TestCase):
    """Test Class Consisting of UI Tests for Ebay App"""


    def setUp(self):
        self.testData = common.getDataFromCSV(testConstants.testDataFile)
        self.mainPage = eBayMainPage.EbayMainPage(self.driver)
        self.loginPage = eBayLoginPage.EbayLoginPage(self.driver)
        self.searchPage = eBaySearchPage.EbaySearchPage(self.driver)
        self.checkOutPage = eBayCheckOutPage.EbayCheckOutPage(self.driver)

    @wrapped_test
    def test_001_verifyPurchaseItem(self):
        """
        Tests if the App Can Be Launched Successfully
        """

        status = self.mainPage.navigateToLoginScreen()
        assert status, "Failed to Navigate to Login Screen..."
        print "Successfully Navigated to Login Screen..."

        status = self.loginPage.login(testConstants.eBayUserName,testConstants.eBayPassword)
        assert status, "Failed to Login..."
        print "Successfully Logged In to eBay App..."

        status = self.mainPage.searchItem(self.testData[1])
        assert status, "Failed to Navigate to Login Screen..."
        print "Successfully Searched item..."

        searchPageTitle, searchpagePrice = self.searchPage.selectRandomSearchResult()
        if not (searchPageTitle or searchpagePrice):
            assert False, "Failed to get item price and item title from search results"

        status = self.checkOutPage.verifyCheckOutPage(searchPageTitle, searchpagePrice)
        assert status, "Failed, Item title and price from search page does not match with that from checkout"

        print "Successfully Verified item details from Search Results Page and Checkout Page..."

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()