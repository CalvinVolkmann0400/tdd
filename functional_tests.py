from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list(self):
        #can open website
        self.browser.get("http://localhost:8000")
        #sees title & header with to-do list
        self.assertIn("To-Do", self.browser.title)
        #sees textbox to enter to-do

        #enter to-do
        
        #hits enter & page update

        #enter another one

        #go home
        self.fail("Finish the test")



if __name__ == '__main__':
    unittest.main()