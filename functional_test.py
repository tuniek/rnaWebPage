from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_start_a_list(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Genus', self.browser.title)
        self.fail('Koniec testów') 

if __name__ =='__main__':
    unittest.main()                  