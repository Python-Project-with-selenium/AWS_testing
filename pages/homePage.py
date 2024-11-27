import pdb
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
from selenium.webdriver.common.action_chains import ActionChains
from utilities.utils import Util_Test
import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import os


class Home_Page:
    def __init__(self, driver):
        self.driver = driver
        self.select_envelope_docx = "//div[contains(text(), " + constants.envelope_file_docx + ")]"
        self.select_envelope_pdf = "//div[contains(text(), " + constants.envelope_file_pdf + ")]"
        self.home_tab = "button[data-qa='header-HOME-tab-button']"
        self.send_documents_for_signature = "/div[@class='css-vrm39m']"
        self.start_button = "//span [contains(text(),'Start')]/parent::button"
        self.envelope_subMenu_btn ="//button[@data-qa='envelopes-submenu-trigger']"
        self.send_envelope_btn = "button[data-qa='manage-sidebar-actions-ndse-send_envelope']"
        self.upload_file_button = "button[data-qa='upload-file-button']"
        self.browse_button = "label[class='css-rpxvy8']"
        self.add_recipients = "button[data-qa='recipients-add']"
        self.signing_order_chkbx = "label[data-qa='recipients-sign-order-checkbox-label']"
        self.recipient_routing_order1 = "(//input[@data-qa='recipient-routing-order'])[1]"
        self.recipient_routing_order2 = "(//input[@data-qa='recipient-routing-order'])[2]"
        self.recipient_name1 = "(//input[@data-qa='recipient-name'])[1]"
        self.recipient_name2 = "(//input[@data-qa='recipient-name'])[2]"
        self.recipient_email1 = "(//input[@data-qa='recipient-email'])[1]"
        self.recipient_email2 = "(//input[@data-qa='recipient-email'])[2]"
        self.recipient_name = "(//input[@data-qa='recipient-name'])[index]"
        self.recipient_email = "(//input[@data-qa='recipient-email'])[index]"
        self.next_button = "button[data-callout='footer-prepare-next-action']"
        self.upload_file_input = "input[data-qa='upload-file-input']"
        self.wootric_close_button = "wootric-close"
        self.add_recipients_content = "button[aria-controls='add-recipients-content']"
        self.select_document = "//div[contains(text(), 'document_name')]"
        self.correct_button = "button[data-qa='status-action-button-correct']"
        self.correct_resend_button = "button[data-qa='footer-simple-correct-resend-link']"
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.approver_name1 = "(//span[@data-qa='recipient-name'])[2]"
        self.approver_name2 = "(//span[@data-qa='recipient-name'])[1]"
        self.recipient_type = "(//button[@data-qa='recipient-type'])[2]"
        self.receive_copy_type = "//span[contains(text(), 'Receives a Copy')]"
        self.signature_field = "button[data-qa='Signature']"
        self.send_button = "button[data-qa='footer-send-button']"
        self.banner_no_thanks_button = "span[data-qa='banner-button-secondary']"
        self.recipient_receiver = "//span[contains(text(), 'Receiver')]"
        self.recipient_status = "//span[contains(text(), 'Receives a Copy')]"
        self.header_sent = "//h1[@data-qa='manage-envelopes-header-title']"
        self.sent_box = "//span[@data-qa='manage-sidebar-labels-sent-label-text']"
        self.correct_button = "//button[@data-qa='status-action-button-correct']"
        self.lock_option = "//span[@data-qa='icon-lock-doclock']"
        self.file_menu_button = "button[data-qa='file-menu']"
        self.delete_document_option = "//button[@data-qa='delete-document']"
        self.wrong_ele = "button[data-qa='sidebar-actions-ndse-trigger']"
        self.action_required = "button[data-qa='action-required-count']"
        self.file_menu_button = "button[data-qa='file-menu']"
        self.recipient_delete = "button[data-qa='recipient-delete']"
        self.recipient_fields_delete = "button[data-qa='modal-confirm-btn']"
        self.change_role_button = "button[data-qa='modal-confirm-btn']"
        self.file_menu_button = "button[data-qa='file-menu']"
        self.replace_menu_item = "//input[@data-qa='replace-document']"
        self.recipient_type1 = "(//button[@data-qa='recipient-type'])[1]"
        self.toast_content = "div[data-qa='ds-toast-content-text']"
        self.correcting_label = "span[data-qa='site-msg-text']"
        self.add_documents_header = "//button[normalize-space()='Add documents']"
        self.replace_document_option = "button[data-qa='rename-document']"
        self.hide_btn = "//button[@data-qa='tutorial-hide-all']"
        self.got_it_btn = "//button[@data-qa='tutorial-got-it']"
        self.docusign_logo = "//img[@data-qa='header-docusign-logo']"
        self.action_required_button = "//button[@data-qa='action-required-count']"
        self.completed_count = "//button[@data-qa='completed-count']"
        self.profile_button_avatar = "//span[@data-qa='header-profile-menu-button-avatar']"
        self.my_preferences = "//button[@data-qa='header-choice-PREFERENCES-button']"
        self.cancel_focus_container = "//div[@data-qa='focus-trap-container']//button[1]"

    def validate_home_page(self):
        max_retries = 2
        retry_count = 0
        while retry_count < max_retries:
            try:
                WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located((
                    By.XPATH, self.docusign_logo))).is_displayed()
                home_tab = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((
                    By.CSS_SELECTOR, self.home_tab))).is_displayed()
                assert home_tab
                WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((
                    By.XPATH, self.start_button))).is_displayed()
                break
            except (StaleElementReferenceException, TimeoutException):
                retry_count += 1
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.action_required_button))).is_displayed()
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.completed_count))).is_displayed()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.cancel_focus_container))).click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.cancel_focus_container))).click()
        except:
            print(" ")

    def click_userprofile_and_preferences(self):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.profile_button_avatar))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((
            By.XPATH, self.my_preferences))).click()

    def click_start_button(self):
        max_retries = 2
        retry_count = 0
        while retry_count < max_retries:
            try:
                WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located((
                    By.XPATH, self.start_button))).is_displayed()
                WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((
                    By.XPATH, self.start_button))).click()
                WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located((
                    By.XPATH, self.envelope_subMenu_btn))).is_displayed()
                WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located((
                    By.XPATH, self.envelope_subMenu_btn))).click()
                break
            except (StaleElementReferenceException, TimeoutException):
                retry_count += 1

    def send_envelope(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((
            By.XPATH, self.envelope_subMenu_btn))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.send_envelope_btn))).click()
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                By.XPATH, self.hide_btn))).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
                By.XPATH, self.got_it_btn))).click()
        except:
            print("No Popup's are available")

