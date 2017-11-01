from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Murat yeni bir to-do uygulaması görür. Anasayfasına gidip siteyi kontrol etmek eder.
        self.browser.get('http://localhost:8000')

        # Sayfanın title'ının To-Do olduğunu görür
        self.assertIn('To-Do', self.browser.title)

        # # Hemen bir To-do item'ı eklemeye davet edilir.
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # # Text box'a "Baget satın al" yazar. (Kendisi bateri çalmaktadır.)
        # inputbox.sendkeys('Baget satın al')

        # # Enter'a bastığında sayfa yenilenir, ve sayfada
        # # "1: Baget satın al" maddesini görünür.
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #                 any(row.text == '1: Baget satın al' for row in rows)
        # )

        # self.fail('Finish the test!')

        # Sayfada hala yeni item ekleme text box'ı bulunur. Buraya "Studyodan zaman kirala" yazar.

        # Sayda yeniden yüklenir. ve iki item'da sayfada listelenir.

        # Sayfadan çıkıp girdiğinde bu listenin korunup korunmayacağını merak eder. Sayfa kendisine bu iş için
        # ürettiği url'i görür.

        # bu URL'i ziyaret eder, ve listesinin hala durduğunu görür.

        # Bu iş tamamdır.



if __name__ == '__main__':
   unittest.main()