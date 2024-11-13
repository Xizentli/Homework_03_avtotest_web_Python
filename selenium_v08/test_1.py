import yaml
import time
from testpage import OperationsHelper
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    """Невозможность аутентификации с невалидными Username и Password"""

    logging.info("Test 1 Starting")     # подключаем логирование

    testpage = OperationsHelper(browser)    # инициализация страницы
    testpage.go_to_site()   # открываем страницу
    testpage.fill_login_field("test")    # ввод данных в поле логина
    testpage.fill_pass_field("test")     # ввод данных в поле пароля
    testpage.click_login_button()   # кликаем на кнопку Login
    time.sleep(testdata["wait"])

    assert testpage.get_error_text() == "401", "test1 FAIL"


def test_step2(browser):
    """Успешная аутентификация с валидными Username и Password"""

    logging.info("Test 2 Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.fill_login_field(testdata["username"])  # ввод данных в поле логина
    testpage.fill_pass_field(testdata["password"])  # ввод данных в поле пароля
    testpage.click_login_button()  # кликаем на кнопку Login
    time.sleep(testdata["wait"])

    assert testpage.get_greeting_text() == "Hello, {}".format(testdata["username"]), "test2 FAIL"


def test_step3(browser):
    """Создание поста"""

    logging.info("Test 3 Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.click_create_new_post_icon()   # клик по иконке Create new post
    time.sleep(testdata["wait"])
    testpage.fill_title_field(testdata["title"])     # ввод данных в поле Title
    testpage.fill_description_field(testdata["description"])  # ввод данных в поле Description
    testpage.fill_content_field(testdata["content"])  # ввод данных в поле Content
    testpage.click_save_button()    # клик по кнопке SAVE
    time.sleep(testdata["wait"])

    assert testpage.get_post_title() == testdata["title"], "test3 FAIL"


def test_step4(browser):
    """Проверка на наличие созданного поста на главной странице"""

    logging.info("Test 4 Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.click_home_button()    # клик по кнопке Home
    time.sleep(testdata["wait"])

    assert testpage.get_title_of_first_post() == testdata["title"], "test4 FAIL"


def test_step5(browser):
    """Проверка на наличие всплывающего окна при взаимодействии с Contact Us"""

    logging.info("Test 5 Starting")

    testpage = OperationsHelper(browser)  # инициализация страницы
    testpage.click_contact_button()  # клик по кнопке Contact
    testpage.fill_your_name_field(testdata["your_name"])    # ввод данных в поле Your name
    testpage.fill_your_email_field(testdata["your_email"])  # ввод данных в поле Your email
    testpage.fill_your_content_field(testdata["your_content"])  # ввод данных в поле Content
    testpage.click_contact_us_button()

    assert testpage.get_alert() == "Form successfully submitted", "test5 FAIL"
