# [FAILED] pytest -v --language=es test_items.py
# [PASSED] pytest -v --language=fr test_items.py 

from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_name_correct_lenguage(browser):
    browser.get(link)

    time.sleep(30)

    button_value = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").text
    assert button_value == "Ajouter au panier", f"Надпись на кнопке '{button_value}', а должна быть - 'Ajouter au panier',"
