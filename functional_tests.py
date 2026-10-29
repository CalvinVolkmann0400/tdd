from selenuim import webdriver
import unitest

class NewVisitorTest(unitest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list(self):
        #can open website
        self.browser.get("http://localhost:8000")
        #sees title & header with to-do list
        self.assertIn
        #sees textbox to enter to-do

        #enter to-do
        
        #hits enter & page update

        #enter another one

        #go home
        self.fail("Finish the test")



if__name__ == '__main__':
    main()




browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Congratulations' in browser.title
print("OK")