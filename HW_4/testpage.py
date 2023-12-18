import logging, time, yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By

identities = dict()
with open('D:\Work\pytests\selenium_webdriver\HW_4\locators.yaml') as f:
    locators = yaml.safe_load(f)
for locator in locators['xpath'].keys():
    identities[locator] = (By.XPATH, locators['xpath'][locator])
for locator in locators['css'].keys():
    identities[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send "{word}" to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operate with {locators}')
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We found text {text} in field {element_name}')
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    # CLICK EVENTS
    def click_save_button(self):
        self.click_button(identities['LOCATOR_SAVE_BTN'], description='save')

    def click_add_post_button(self):
        self.click_button(identities['LOCATOR_NEW_POST_BTN'], description='new post')

    def click_contact(self):
        self.click_button(identities['LOCATOR_CONTACT_SEND'], description='contact')

    def click_contact_button(self):
        self.click_button(identities['LOCATOR_CONTACT_BTN'], description='send')

    def click_login_button(self):
        self.click_button(identities['LOCATOR_LOGIN_BTN'], description='login')

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(identities['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(identities['LOCATOR_PASS_FIELD'], word, description='password form')

    def add_title(self, string):
        self.enter_text_into_field(identities['LOCATOR_TITLE'], string, description='title')

    def add_description(self, string):
        self.enter_text_into_field(identities['LOCATOR_DESCRIPTION'], string, description='description')

    def add_content(self, string):
        self.enter_text_into_field(identities['LOCATOR_CONTENT'], string, description='description')

    def add_name(self, string):
        self.enter_text_into_field(identities['LOCATOR_CONTACT_NAME'], string, description='contact_name')

    def add_email(self, string):
        self.enter_text_into_field(identities['LOCATOR_CONTACT_EMAIL'], string, description='contact_email')

    def add_contact_content(self, string):
        self.enter_text_into_field(identities['LOCATOR_CONTACT_CONTENT'], string, description='contact_content')

    # GET TEXT
    def new_post_title(self):
        return self.get_text_from_element(identities['LOCATOR_FIND_NEW_POST'], description='new_post_title')

    def get_error_text(self):
        return self.get_text_from_element(identities['LOCATOR_ERROR_FIELD'], description='error label')

    def login_success(self):
        return self.get_text_from_element(identities['LOCATOR_HELLO'], description='username')

    def get_alert_message(self):
        time.sleep(2)
        logging.info('Get alert message')
        text = self.get_alert_text()
        logging.debug(f'Alert message is {text}')
        return text
