from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from testData.constants import comment_field
from pages.loginPage import Login_Page
import time


class Add_Sign_Tags:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.home_tab = "//button[@data-qa='header-HOME-tab-button']"
        self.signature_tag_field = "button[data-qa='Signature']"
        self.select_recipient = "//button[@data-qa='recipient-index']"
        self.send_button = "button[data-qa='footer-send-button']"
        self.recipient_selector = "button[data-qa='recipient-selector']"
        self.formatting_button = "//span[contains(text(), 'Formatting')]"
        self.dimension_scale = "//input[@data-qa='data-dimension-scale']"
        self.no_thanks_link = "//span[@data-qa='banner-button-secondary-text']"
        self.docusign_logo = "img[data-qa='header-docusign-logo']"
        self.send_without_field = "button[data-qa='send-without-fields']"
        self.error_message_without_sign_tags = "//div[@data-qa='ds-toast-content-text']"
        self.actions_menu_button = "//button[@data-qa='other-actions-menu-button']"
        self.save_close_button = "//button[@data-qa='save-and-close']"
        self.document_page = "//div[@data-qa='document-page-full']"
        self.correct_resend_button = "button[data-qa='footer-simple-correct-resend-link']"
        self.Text_field = "button[data-qa='Text']"
        # Validating the option under Signature section
        self.formatting_option = "//span[contains(text(),'Formatting')]"
        self.datalabel_option = "//span[contains(text(),'Data Label')]"
        self.tooltip_option = "//span[contains(text(),'Tooltip')]"
        self.location_option = "//span[contains(text(),'Location')]"
        self.recipient_option = "//button/span[contains(text(),'Recipient')]"
        # validating options under actions Drop Down under Add sign page
        self.discard_button = "//button[@data-qa='discard-delete']"
        self.edit_message_button = "//span[@data-qa='edit-message-text']"
        self.edit_recepient_button = "//span[@data-qa='edit-message-text']"
        self.edit_document_button = "//span[@data-qa='edit-documents-text']"
        self.advanced_options_button = "//span[@data-qa='edit-advanced-options-text']"
        self.successful_msg = "//div[@data-qa='ds-toast-content-text']/span[1]"

    def select_signer(self, index_number):
        WebDriverWait(self.driver, 45).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.recipient_selector))).click()
        select_recipient = self.select_recipient.replace('index', index_number)
        WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located((By.XPATH, select_recipient)))
        WebDriverWait(self.driver, 45).until(
            EC.element_to_be_clickable((By.XPATH, select_recipient))).click()

    def addSignatureTag(self, x_axis):
        source = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signature_tag_field)))
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(x_axis, 180).pause(1).move_by_offset(-10, -10).release().perform()
        time.sleep(2)

    def saveAndCloseTemplateWithActionButton(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.actions_menu_button))).click()
        assert all(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.save_close_button, self.discard_button, self.edit_message_button, self.edit_recepient_button,
                    self.edit_document_button, self.advanced_options_button])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.save_close_button))).click()

    def click_send_btn(self):
        send_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_button)))
        assert send_btn.is_displayed(), "Send button is not displayed"
        assert send_btn.is_enabled(), "Send button is not clickable"
        send_btn.click()
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                By.XPATH, self.no_thanks_link))).click()
        except:
            print("No thanks link is not available")
        try:
            success_message = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                By.XPATH, self.successful_msg))).text
            assert constants.success_message in success_message
        except:
            print("assertion failure")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.home_tab))).click()

    def validateOptionsUnderSignature(self):
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.formatting_option, self.location_option, self.tooltip_option, self.datalabel_option,
                    self.recipient_option])

    def change_sign_tag_size(self, size="200"):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.formatting_button))).click()
        dimension_scale = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.dimension_scale)))
        dimension_scale.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        dimension_scale.send_keys(Keys.DELETE)
        time.sleep(1)
        dimension_scale.send_keys(size)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.formatting_button))).click()
        time.sleep(1)

    def send_envelop_without_sign_tags(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_button))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.send_without_field))).click()
        error_message_text = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.error_message_without_sign_tags))).text
        assert error_message_text == constants.error_message_when_without_sign_tag
        print('Error message:', error_message_text)
        time.sleep(2)

    def clickCorrectToResendDocument(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.correct_resend_button))).click()
        time.sleep(2)

    def scroll_to_next_envelope(self):
        scroll_page = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.document_page)))
        scroll_page.click()
        scroll_origin = ScrollOrigin.from_element(scroll_page)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 1150).perform()

    def add_comment_field(self):
        source = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.Text_field)))
        action = ActionChains(self.driver)
        action.click_and_hold(source).perform()

        # Get the dimensions of the document page
        document_page = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.document_page)))
        page_width, page_height = document_page.size.get('width'), document_page.size.get('height')
        print("Document page width and page height =", page_width, page_height)
        # Calculate the desired position based on the page dimensions
        x_offset = int(page_width * 0.7)  # 60% of the page width
        y_offset = int(page_height * -0.1)  # 20% of the page height
        print(x_offset, y_offset)

        action.move_by_offset(x_offset, y_offset).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(2)