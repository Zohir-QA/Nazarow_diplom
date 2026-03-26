from selenium.webdriver.common.by import By

class MainPageLocators:
    URL = "http://papapizza59.ru/"
    MODAL_WINDOW = (By.XPATH, '//a[@class="popup-modal-dismiss"]')
    DELIVERY_TERMS = (By.XPATH, '//a[text() = "Условия доставки" and not(@rel="nofollow")]')
    STOCK = (By.XPATH, '//a[@href="http://papapizza59.ru/nashi_akcii" and not(@rel="nofollow")]') # Кнопка на шапке акции
    PAYMENT = (By.XPATH, '//div[contains(@class, "top-links")]//a[@href="http://papapizza59.ru/oplata"]') # Кнопка на шапке плата
    OUR_PROMOTIONS = (By.XPATH, '//h1[text() = "Наши акции"]') # Заголовок на вкладке акции
    DELIVERY = (By.XPATH, '//h1[text() = "Доставка"]') # Заголовок на вкладке доставка
    PAYMENT_HEADER = (By.XPATH, '//h1[text() = "Оплата"]') # Заголовок на вкладке оплата
    PIZZA_BUTTON_NAVBAR = (By.XPATH, '//a [@href="http://papapizza59.ru/picca/" and not(@rel="nofollow")]') # Кнопка в навигационном меню пицца
    PIZZA_HEADER = (By.XPATH, '//h1 [text()="Пицца с доставкой в Перми"]') # Заголовок на вкладке пицца
    MAIN_IMAGE = (By.XPATH, '//a[@href="http://papapizza59.ru/"]//img') # Изображение на главной
    MAIN_TITLE = (By.XPATH, '//h1[@class="home_h1"]') # Заголовок на главной
    DRINKS_BUTTON_NAVBAR = (By.XPATH, '//a[@href="http://papapizza59.ru/napitki/" and not(@rel="nofollow") and not(@class="list-group-item")]') # Категория напитки
    DRINKS_HEADER = (By.XPATH, '//h1 [text()="Напитки"]') # Заголовок на вкладке напитки
    HOT_SNACKS_NAVBAR = (By.XPATH, '//a[@href="http://papapizza59.ru/goryachie_zakuski/" and not(@rel="nofollow") and not(@class="list-group-item")]') # Категория горячих закусок
    HOT_SNACKS_HEADER = (By.XPATH, '//h1[text()="Горячие закуски"]') # Заголовок на вкладке горячие закуски
    COMBO_NAVBAR = (By.XPATH, '//a[@href="http://papapizza59.ru/kombo/" and not(@rel="nofollow") and not(@class="list-group-item")]') # Категория комбо
    COMBO_HEADER = (By.XPATH, '//h1[text() = "Заказать выгодное комбо из пицц — доставка в Перми"]') # Заголовок на вкладке горячие комбо
    PIZZA_SAUCES_NAVBAR = (By.XPATH, '//a[@href="http://papapizza59.ru/sousy_k_picce/" and not(@rel="nofollow") and not(@class="list-group-item")]') # Категория соусы к пицце
    PIZZA_SAUCES_HEADER = (By.XPATH, '//h1[text() = "Соусы к пицце"]') # Заголовок на вкладке горячие комбо




