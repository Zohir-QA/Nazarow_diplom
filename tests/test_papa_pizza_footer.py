import allure
import pytest
from pages.page_main import LoginPage

@allure.id("005")
@allure.label("Papa pizza")
@allure.title("Papa pizza проверка подвала сайта")
@allure.description("Тест проверяет что пользователь проходит до карточки товара и добавляет в корзину")
@pytest.mark.papa_pizza

def tests_005(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Скролим до подвала'):
        login.scroll_footer()

    with allure.step('Кликнуть на кнопку "Пиццерия"'):
        login.click_pizzeria_button()

    with allure.step('Проверяем что мы во вкладке "Пиццерия"'):
        assert login.wait_pizzeria_header(), "ОШИБКА не перешел по вкладке пиццерия"

    with allure.step('Скролим до подвала'): # для экранов 1280×720 и ниже
        login.scroll_footer()

    with allure.step('Кликнуть на кнопку "Условия бесплатной доставки"'):
        login.click_free_shipping_conditions_button()

    with allure.step('Проверяем что мы во вкладке "Доставка"'):
        assert login.wait_delivery_header(), "ОШИБКА не перешел по вкладке доставка"

    with allure.step('Скролим до подвала'):
        login.scroll_footer()

    with allure.step('Кликнуть на кнопку "Оплата"'):
        login.click_payment_button_footer()

    with allure.step('Проверяем что мы во вкладке "Оплата" успешно открыта'):
        assert login.wait_payment_header(), "ОШИБКА не перешел по вкладке оплата"

    with allure.step('Скролим до подвала'): # для экранов 1280×720 и ниже
        login.scroll_footer()

    with allure.step('Кликнуть на кнопку "Политика конфиденциальности"'):
        login.click_privacy_policy_button()

    with allure.step('Проверяем что мы во вкладке "Политика конфиденциальности'):
        assert login.wait_privacy_policy_header(), "ОШИБКА не перешел по вкладке политика конфиденциальности"

    with allure.step('Скролим до подвала'):
        login.scroll_footer()

    with allure.step('Кликнуть на кнопку "Публичная оферта"'):
        login.click_public_offer_button()

    with allure.step('Проверяем что мы во вкладке "Оферта'):
        assert login.wait_offer_header(), "ОШИБКА не перешел по вкладке оферта"