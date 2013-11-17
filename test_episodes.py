from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, datetime

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMet1(self):
#         driver = webdriver.Chrome()
        driver = webdriver.Chrome()
        driver.get("http://next-episode.net")
        episodes = ['Elementary', 'How I Met Your Mother', 'Two and a Half Men', "Grey's Anatomy", "The Vampire Diaries"]
        driver.maximize_window()
        assert "Next Episode" in driver.title
        now = datetime.datetime.now()
        crt_date = now.strftime("%d/%m")
        f = open('episode_list', 'w')
        f.write(crt_date + "\n")
        for episode in episodes:
            driver.find_element_by_link_text(episode).click()
            assert episode in driver.title
            ep_date = driver.find_element_by_xpath(".//*[@id='resizeTable']/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]").text
            ep_season = driver.find_element_by_xpath(".//*[@id='resizeTable']/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[3]/td[2]").text
            ep_nr = driver.find_element_by_xpath(".//*[@id='resizeTable']/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td[2]").text
            new_episode = episode + " " + ep_season + " " + ep_nr + " " + ep_date[3:10]
            f.write(new_episode + "\n")
        f.close()
        driver.close()

if __name__ == '__main__':
    unittest.main()
