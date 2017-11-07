from django.test import LiveServerTestCase
from selenium import webdriver
# import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Murat yeni bir to-do uygulaması görür. Anasayfasına gidip siteyi kontrol etmek eder.
        self.browser.get(self.live_server_url)

        # Sayfanın title'ının To-Do olduğunu görür
        self.assertIn('To-Do', self.browser.title)

        # Hemen bir To-do item'ı eklemeye davet edilir.
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Text box'a "Baget satın al" yazar. (Kendisi bateri çalmaktadır.)
        inputbox.send_keys('Baget satın al')

        # Enter'a bastığında sayfa yenilenir, ve sayfada
        # "1: Baget satın al" maddesini görünür.
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Baget satın al')

        # Sayfada hala yeni item ekleme text box'ı bulunur. Buraya "Studyodan zaman kirala" yazar.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Studyodan zaman kirala')
        inputbox.send_keys(Keys.ENTER)

        # Sayda yeniden yüklenir. ve iki item'da sayfada listelenir.
        self.check_for_row_in_list_table('1: Baget satın al')
        self.check_for_row_in_list_table('2: Studyodan zaman kirala')

        # Sayfadan çıkıp girdiğinde bu listenin korunup korunmayacağını merak eder. Sayfa kendisine bu iş için
        # ürettiği url'i görür.

        # bu URL'i ziyaret eder, ve listesinin hala durduğunu görür.

        # Bu iş tamamdır.


        self.fail('Finish the test!')
