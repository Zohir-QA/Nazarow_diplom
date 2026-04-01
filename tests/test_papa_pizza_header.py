import allure
import pytest
from pages.page_main import LoginPage

@allure.id("001")
@allure.label("Papa pizza")
@allure.title("Papa pizza проверка шапки сайта")
@allure.description("Тест проверяет что пользователь может перемещаться корректно в шапке сайта")
@pytest.mark.papa_pizza
@pytest.mark.parametrize("driver", ["edge", "chrome"], indirect=True)

def tests_001(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Кликнуть на кнопку "Акции"'):
        login.click_stock()

    with allure.step('Проверяем что вкладке "Акции" успешно открыта'):
        assert login.wait_our_promotions(), "ОШИБКА не перешел по вкладке акции"

    with allure.step('Кликнуть на кнопку "Условия доставки"'):
        login.click_delivery_terms()

    with allure.step('Проверяем что вкладке "Условия доставки" успешно открыта'):
        assert login.wait_delivery_header(), "ОШИБКА не перешел по вкладке условия доставки"

    with allure.step('Кликнуть на кнопку "Оплата"'):
        login.click_payment()

    with allure.step('Проверяем что вкладке "Оплата" успешно открыта'):
        assert login.wait_payment_header(), "ОШИБКА не перешел по вкладке оплата"

    login.take_screenshot('Страница "Оплаты"')
