import logging, yaml
from testpage import OperationsHelper

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info('Start login negative test')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test_login_negative FAILED'


def test_login_positive(browser):
    logging.info('Start login positive test')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.login_success() == f'Hello, {testdata["login"]}', 'test_login_positive FAILED'


def test_create_post(browser):
    logging.info('Start create post test')
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata['login'])
    # testpage.enter_pass(testdata['password'])
    # testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata['title'])
    testpage.add_description(testdata['description'])
    testpage.add_content(testdata['content'])
    testpage.click_save_post_button()
    testpage.go_to_site()
    assert testpage.find_new_post_title() == f'{testdata["title"]}', 'test_create_post FAILED!'


def test_contact_us(browser):
    logging.info('Start contact us test')
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["password"])
    # testpage.click_login_button()
    testpage.click_contact_button()
    testpage.add_name(testdata['user_name'])
    testpage.add_email(testdata['user_email'])
    testpage.add_contact_content(testdata['content_contact'])
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == 'Form successfully submitted', 'test contact us FAILED!'
