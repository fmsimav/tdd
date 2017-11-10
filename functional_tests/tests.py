from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.test import LiveServerTestCase
from selenium import webdriver
# import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium .common.exceptions import WebDriverException

MAX_WAIT = 3
DEBUG_WAIT_TIME = 0
CHROME_DRIVER_PATH = '/Users/msimav/anaconda/envs/python/bin/chromedriver'


# class NewVisitorTest(LiveServerTestCase):
class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(CHROME_DRIVER_PATH)

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')

                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Murat yeni bir to-do uygulaması görür. Anasayfasına gidip siteyi kontrol etmek eder.
        self.browser.get(self.live_server_url)

        time.sleep(DEBUG_WAIT_TIME)
        # Sayfanın title'ının To-Do olduğunu görür
        self.assertIn('To-Do', self.browser.title)

        # Hemen bir To-do item'ı eklemeye davet edilir.
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Text box'a "Baget satın al" yazar. (Kendisi bateri çalmaktadır.)
        inputbox.send_keys('Baget satın al')
        time.sleep(DEBUG_WAIT_TIME)
        # Enter'a bastığında sayfa yenilenir, ve sayfada
        # "1: Baget satın al" maddesini görünür.
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Baget satın al')

        # Sayfada hala yeni item ekleme text box'ı bulunur. Buraya "Studyodan zaman kirala" yazar.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Studyodan zaman kirala')
        time.sleep(DEBUG_WAIT_TIME)
        inputbox.send_keys(Keys.ENTER)

        # Sayda yeniden yüklenir. ve iki item'da sayfada listelenir.
        time.sleep(DEBUG_WAIT_TIME)
        self.wait_for_row_in_list_table('1: Baget satın al')
        self.wait_for_row_in_list_table('2: Studyodan zaman kirala')

    def test_can_start_a_list_for_one_user(self):

        # Edith has heard about a cool new online to-do app. She goes
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('Buy peacock feathers')
        time.sleep(DEBUG_WAIT_TIME)
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        time.sleep(DEBUG_WAIT_TIME)
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

    def test_multiple_users_can_start_lists_at_different_urls(self):

        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')

        time.sleep(DEBUG_WAIT_TIME)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(DEBUG_WAIT_TIME)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # Sayfadan çıkıp girdiğinde bu listenin korunup korunmayacağını merak eder. Sayfa kendisine bu iş için ürettiği url'i görür.

        murat_list_url = self.browser.current_url
        time.sleep(DEBUG_WAIT_TIME)
        self.assertRegex(murat_list_url, '/lists/\d+/')

        # bu URL'i ziyaret eder, ve listesinin hala durduğunu görür.

        ## sonra başka bir kullanıcı gelir.
        ## cookie ve post datalardan kurtulmak için yeni bir tarayıcı session'ı başlatırak kontrol ediyoruz.

        self.browser.quit()
        self.browser = webdriver.Chrome(CHROME_DRIVER_PATH)

        # Ahmet siteye gelir, Murat'ın listesindeki bilgileri görmez.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        time.sleep(DEBUG_WAIT_TIME)
        self.assertNotIn('Buy peacock feathers', page_text)

        # Ahmet yeni bir liste oluşturur.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')

        time.sleep(DEBUG_WAIT_TIME)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(DEBUG_WAIT_TIME)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Ahmet'e yeni bir URL oluştutulur
        ahmet_list_url = self.browser.current_url
        time.sleep(DEBUG_WAIT_TIME)
        self.assertRegex(ahmet_list_url, '/lists/\d+/')
        self.assertNotEqual(ahmet_list_url, murat_list_url)

        # sayfada yine murat'ın listesinden madde görmez
        page_text = self.browser.find_element_by_tag_name('body').text
        time.sleep(DEBUG_WAIT_TIME)
        self.assertNotIn('Baget satın al', page_text)
        self.assertIn('Buy milk', page_text)

        # Bu iş tamamdır.

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
