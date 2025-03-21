import allure
from behave import given, when, then
from selenium import webdriver
from features.pages.login_page import LoginPage


@given("користувач відкриває сторінку логіна")
@allure.step("Відкриття сторінки логіна")
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.page = LoginPage(context.driver)
    context.page.open("https://example.com/login")


@when('він вводить "{email}" і "{password}"')
@allure.step("Введення облікових даних: {email} / {password}")
def enter_credentials(context, email, password):
    context.page.enter_email(email)
    context.page.enter_password(password)
    context.page.click_login()


@then('він бачить повідомлення "{expected_message}"')
@allure.step("Перевірка повідомлення після логіну: {expected_message}")
def verify_login_success(context, expected_message):
    actual_message = context.page.get_success_message()

    if actual_message != expected_message:
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="Login Failure",
                      attachment_type=allure.attachment_type.PNG)

    assert actual_message == expected_message, f"Очікувалось '{expected_message}', а отримано '{actual_message}'"
    context.driver.quit()
