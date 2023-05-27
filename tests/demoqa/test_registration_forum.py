import allure

from pages.registration_pages import RegistrationPage


@allure.title("Тест регистрации формы")
def test_successful(setup_browser):
    browser = setup_browser
    registration_page = RegistrationPage(browser)

    with allure.step("Открытие браузера"):
        browser.open("https://demoqa.com/automation-practice-form")

    with allure.step("Заполнение регистрационных даных"):
        registration_page.fill_first_name("Albert")
        registration_page.fill_last_name("Ivanov")
        registration_page.fill_email("ALLIIVAN@mail.ru")
        registration_page.fill_number("8954567689")
        registration_page.choice_gender('Male')
        registration_page.fill_date_of_birth('1993', 'November', '28')
        registration_page.choice_subject('Physics')
        registration_page.choice_hobbies('Sports')
        registration_page.choice_hobbies_more('Reading')
        registration_page.choice_hobbies_more_more('Music')
        registration_page.choice_pictures('pictures.jpg')
        registration_page.remove_block()
        registration_page.fill_adress('Pharabi street 18')
        registration_page.fill_state('Rajasthan')
        registration_page.fill_city('Jaipur')

    with allure.step("Проверка регистрационных данных"):
        registration_page.assert_register_user_info(
            'Albert Ivanov',
            'ALLIIVAN@mail.ru',
            'Male',
            '8954567689',
            '28 November,1993',
            'Physics',
            'Sports, Reading, Music',
            'picture',
            'Pharabi street 18',
            'Rajasthan Jaipur')
