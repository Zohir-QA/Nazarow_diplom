import allure
import pytest
from pages.page_main import LoginPage

@allure.id("004")
@allure.label("Papa pizza")
@allure.title("Papa pizza проверка карточки товара")
@allure.description("Тест проверяет что пользователь может перемещаться корректно по подвалу")
@pytest.mark.parametrize("driver", ["edge", "chrome"], indirect=True)

def tests_004(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Скролим до карточки товара "Супермясная"'): # для экранов 1280×720 и ниже
        login.scroll_caption_product()

    with allure.step('Кликнуть на карточки товара "Супермясная"'):
        login.click_caption_product()

    with allure.step('Кликнуть на кнопку "L (38 см)"'):
        login.click_size_l_button()

    with allure.step('Скролим до кнопки "В корзину"'):
        login.scroll_cart_button()

    with allure.step('Кликнуть на кнопку "В корзину"'):
        login.click_cart_button()

    with allure.step('Кликнуть на кнопку "Оформить заказ"'):
        login.click_place_order_button()

    with allure.step('Проверяем что заказ добавился в корзину'):
        assert login.wait_buyer_form_title(), "ОШИБКА заказ не добавился в корзину"

    login.take_screenshot('Страница "Оформление заказа"')