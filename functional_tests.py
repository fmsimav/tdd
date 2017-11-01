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
        self.fail('Finish the test!')

        # Hemen bir To-do item'ı eklemeye davet edilir.

        # Text box'a "Baget satın al" yazar. (Kendisi bateri çalmaktadır.)

        # Enter'a bastığında sayfa yenilenir, ve sayfada
        # "1: Baget satın al" maddesini görünür.

        # Sayfada hala yeni item ekleme text box'ı bulunur. Buraya "Studyodan zaman kirala" yazar.

        # Sayda yeniden yüklenir. ve iki item'da sayfada listelenir.

        # Sayfadan çıkıp girdiğinde bu listenin korunup korunmayacağını merak eder. Sayfa kendisine bu iş için
        # ürettiği url'i görür.

        # bu URL'i ziyaret eder, ve listesinin hala durduğunu görür.

        # Bu iş tamamdır.

if __name__ == '__main__':
   unittest.main()