import allure
import pytest
from pages.page_main import LoginPage

@allure.id("003")
@allure.label("Papa pizza")
@allure.title("Papa pizza проверка навигационного меню")
@allure.description("Тест проверяет что пользователь может перемещаться корректно по навигационное меню")
@pytest.mark.papa_pizza
@pytest.mark.parametrize("driver", ["edge", "chrome"], indirect=True)

def tests_003(driver):
    login = LoginPage(driver)
    with allure.step("Открываем сайт Papa pizza"):
        login.open()

    with allure.step('Кликнуть "Да" в модальном окне'):
        login.click_modal_window()

    with allure.step('Кликнуть в навигационном меню на кнопку "Пицца"'):
        login.click_pizza_button_navbar()

    with allure.step('Проверяем что мы во вкладке "Пицца"'):
        assert login.wait_pizza_header(), "ОШИБКА не перешел по вкладке пицца"

    with allure.step('Кликнуть в навигационном меню на кнопку "Напитки"'):
        login.click_drinks_button_navbar()

    with allure.step('Проверяем что мы во вкладке "Напитки"'):
        assert login.wait_drinks_header(), "ОШИБКА не перешел по вкладке напитки"

    with allure.step('Кликнуть в навигационном меню на кнопку "Горячие закуски"'):
        login.click_hot_snacks_navbar()

    with allure.step('Проверяем что мы во вкладке "Горячие закуски"'):
        assert login.wait_hot_snacks_header(), "ОШИБКА не перешел по вкладке горячие закуски"

    with allure.step('Кликнуть в навигационном меню на кнопку "Комбо"'):
        login.click_combo_navbar()

    with allure.step('Проверяем что мы во вкладке "Комбо"'):
        assert login.wait_combo_header(), "ОШИБКА не перешел по вкладке комбо"

    with allure.step('Кликнуть в навигационном меню на кнопку "Соусы к пицце"'):
        login.click_pizza_sauces_navbar()

    with allure.step('Проверяем что мы во вкладке "Соусы к пицце"'):
        assert login.wait_pizza_sauces_header(), "ОШИБКА не перешел по cоусы к пицце"

    login.take_screenshot('Страница "Соусы к пицце"')

















