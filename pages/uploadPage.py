import pdb
from pathlib import Path

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
from selenium.webdriver.common.action_chains import ActionChains
from utilities.utils import Util_Test
import time
import os


class Upload_Page:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Util_Test(driver)
        self.home_tab = "button[data-qa='header-HOME-tab-button']"
        self.upload_file_button = "button[data-qa='upload-file-button']"
        self.add_recipients = "button[data-qa='recipients-add']"
        self.signing_order_checkbox = "label[data-qa='recipients-sign-order-checkbox-label']"
        self.recipient_routing_order = "(//input[@data-qa='recipient-routing-order'])[index]"
        self.recipient_name = "(//input[@data-qa='recipient-name'])[index]"
        self.recipient_email = "(//input[@data-qa='recipient-email'])[index]"
        self.next_button = "button[data-callout='footer-prepare-next-action']"
        self.upload_file_input = "input[data-qa='upload-file-input']"
        self.wootric_close_button = "wootric-close"
        self.add_recipients_content = "button[aria-controls='add-recipients-content']"
        self.select_document = "//button[@aria-label='Complete with Docusign: document_name']"
        self.select_template = "//span[@title='document_name']"
        self.correct_resend_button = "button[data-qa='footer-simple-correct-resend-link']"
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.approver_name1 = "(//span[@data-qa='recipient-name'])[1]"
        self.approver_name2 = "(//span[@data-qa='recipient-name'])[2]"
        self.recipient_type = "(//button[@data-qa='recipient-type'])[2]"
        self.receive_copy_type = "//span[contains(text(), 'Receives a Copy')]"
        self.signature_field = "button[data-qa='Signature']"
        self.send_button = "button[data-qa='footer-send-button']"
        self.banner_no_thanks_button = "span[data-qa='banner-button-secondary']"
        self.recipient_receiver = "(//span[@data-qa='recipient-name'])[2]"
        self.recipient_status = "//span[contains(text(), 'Receives a Copy')]"
        self.header_sent = "//h1[@data-qa='manage-envelopes-header-title']"
        self.sent_box = "//span[@data-qa='manage-sidebar-labels-sent-label-text']"
        self.correct_button = "//button[@data-qa='status-action-button-correct']"
        self.lock_option = "//span[@data-qa='icon-lock-doclock']"
        self.file_menu_button = "button[data-qa='file-menu']"
        self.wrong_ele = "button[data-qa='sidebar-actions-ndse-trigger']"
        self.action_required = "button[data-qa='action-required-count']"
        self.recipient_delete = "button[data-qa='recipient-delete']"
        self.recipient_fields_delete = "button[data-qa='modal-confirm-btn']"
        self.change_role_button = "button[data-qa='modal-confirm-btn']"
        self.recipient_type1 = "(//button[@data-qa='recipient-type'])[1]"
        self.toast_content = "div[data-qa='ds-toast-content-text']"
        self.correcting_label = "span[data-qa='site-msg-text']"
        self.add_documents_header = "//button[normalize-space()='Add documents']"
        self.hide_btn = "//button[@data-qa='tutorial-hide-all']"
        self.got_it_btn = "//button[@data-qa='tutorial-got-it']"
        self.docusign_logo = "//img[@data-qa='header-docusign-logo']"
        self.primary_sign_button = "button[data-qa='status-action-button-sign']"
        # Buttons For Sender In DocumentDetailPage
        self.correct_option = "//span[contains(text(),'Correct')]"
        self.move_option = "//span[contains(text(),'Move')]"
        self.resend_option = "//span[contains(text(),'Resend')]"
        self.more_option = "//span[contains(text(),'More')]"
        # Recipient Actions under recipient dropdown
        self.update_recipient_btn = "//button[@data-qa='intermediaries']"
        self.need_to_view_btn = "//button[@data-qa='certifiedDeliveries']"
        self.specify_recipient_btn = "//button[@data-qa='agents']"
        self.allow_to_edit_btn = "//button[@data-qa='editors']"
        self.need_to_sign_btn = "//button[@data-qa='signers']"
        # file options under more ...
        self.apply_templates_btn = "//button[@data-qa='manage-applied-templates']"
        self.replace_menu_item = "//input[@data-qa='replace-document']"
        self.download_document_btn = "//a[@data-qa='download-document']"
        self.rename_document_btn = "//button[@data-qa='rename-document']"
        self.delete_document_btn = "//button[@data-qa='delete-document']"
        self.view_document_btn = "//button[@data-qa='view-document']"
        self.recipient_menu = "button[data-qa='recipient-menu']"
        self.access_code = "//span[contains(text(), 'Add access code')]"
        self.access_code_input = "//input[@data-qa='auth-accessCode-input']"
        self.popup_ok = "//button[@class='css-1osb1sb']"

    def upload_envelope_documents(self, filename, wootricPopup=False, root_directory=None):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.upload_file_button))).click()
        browse_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.upload_file_input)))
        if root_directory is None:
            root_directory = os.getcwd()
            relative_path = Path(filename)
            document_path = root_directory / relative_path
            #print("Document path =", document_path)
            file_path = Path(document_path)
            document_path = str(file_path)
            browse_button.send_keys(document_path)
            time.sleep(2)

        if wootricPopup:
            self.driver.find_element(By.ID, self.wootric_close_button).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.add_recipients_content)

    def clickSetSigningOrderCheckbox(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signing_order_checkbox))).click()

    def addRecipient(self, name, email, number):
        recipient_name1 = self.recipient_name.replace('index', number)
        recipient_email1 = self.recipient_email.replace('index', number)
        if number != constants.index_one:
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, self.add_recipients).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, recipient_name1))).send_keys(name)
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, recipient_email1))).send_keys(email)
        time.sleep(2)

    def set_routing_order(self, actual_order, priority_order):
        routing_order = self.recipient_routing_order.replace('index', actual_order)
        print("routing_order:", routing_order)
        change_routing_order = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, routing_order)))
        change_routing_order.send_keys(Keys.BACKSPACE)
        change_routing_order.send_keys(priority_order)
        time.sleep(2)

    def click_next_btn(self):
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.next_button))).click()

    def verifyCorrectedRoutedOrder(self, fileName):
        first_signer_name = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.approver_name1))).text
        print("first_signer_name:", first_signer_name)
        assert first_signer_name == constants.signer2_name
        second_signer_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.approver_name2))).text
        print("second_signer_name:", second_signer_name)
        assert second_signer_name == constants.signer1_name

    def SelectRecipientAction(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_type))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.receive_copy_type))).click()
        time.sleep(2)

    def verifyOptionsInRecipientType_DD(self):
        # Define XPaths for each recipient action
        recipientActions = [
            self.need_to_sign_btn,
            self.receive_copy_type,
            self.need_to_view_btn,
            self.specify_recipient_btn,
            self.allow_to_edit_btn,
            self.update_recipient_btn
        ]  # Use list comprehension to check if each option is displayed and clickable
        assert all(WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))).is_displayed() for xpath in recipientActions)

    def updateRecipientAction(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_type1))).click()
        self.verifyOptionsInRecipientType_DD()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.receive_copy_type))).click()
        time.sleep(2)
        self.utils.getscreenshot("/3.change_Recipient_Type.png")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.change_role_button))).click()

    def verifyRecipientActionInDocumentDetailPage(self, receiverName, recipientStatus):
        Recipient_Name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_receiver))).text
        print(Recipient_Name)
        assert Recipient_Name == receiverName
        Recipient_Status = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_status))).text
        print(Recipient_Status)
        assert Recipient_Status == recipientStatus

    def click_file_menu(self):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.file_menu_button))).click()

    def verifyOptionsUnderFileMenu(self):
        more_options_xpath = [
            self.apply_templates_btn,
            self.replace_menu_item,
            self.download_document_btn,
            self.rename_document_btn,
            self.delete_document_btn,
            self.view_document_btn
        ]
        assert all(WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))).is_displayed() for xpath in more_options_xpath)

    def restrict_document_del_and_replace(self):
        lock_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.lock_option)))
        assert lock_button.is_displayed()
        self.click_file_menu()
        self.verifyOptionsUnderFileMenu()
        time.sleep(2)
        delete_button_verify = self.driver.find_element(By.XPATH, self.delete_document_btn)
        delete_button_disabled = delete_button_verify.get_attribute("aria-disabled")
        assert delete_button_disabled
        print("Delete button is disabled")
        # Util_Test.getscreenshot("/Delete_button_disabled.png")
        replace_button_verify = self.driver.find_element(By.XPATH, self.replace_menu_item)
        replace_button_disabled = replace_button_verify.get_attribute("aria-disabled")
        assert replace_button_disabled
        print("Replace button is disabled")

    def navigateToEnvelope(self, fileName, sender=False):
        home_tab = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.home_tab)))
        home_tab.click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.manage_tab))).click()
        if sender:
            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, self.sent_box))).click()
            time.sleep(10)
        else:
            time.sleep(10)
        select_doc = self.select_document.replace("document_name", fileName)
        print("document xpath =", select_doc)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, select_doc))).click()
        time.sleep(2)

    def handle_popup(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_ok))).click()


    def navigateToTemplate(self, fileName):
        time.sleep(10)
        select_doc = self.select_template.replace("document_name", fileName)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, select_doc))).click()
        time.sleep(2)

    def verifyButtonsForSenderInDocumentDetailPage(self):
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.correct_option, self.move_option, self.resend_option, self.more_option])

    def correctingDocumentDetails(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.correct_button))).click()

    def scrollToRecipients(self):
        signing_order_checkbox = WebDriverWait(self.driver, 45).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signing_order_checkbox)))
        self.driver.execute_script("arguments[0].scrollIntoView();", signing_order_checkbox)

    def delete_recipient(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.recipient_delete))).click()
        time.sleep(2)
        self.utils.getscreenshot("/1.Delete_Existing_Recipient.png")
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.recipient_fields_delete))).click()

    def validate_toast_msg(self, msg):
        toast_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.toast_content))).text
        print("toastmsg = " + toast_msg)
        assert msg in toast_msg

    def verifyEnvelopeCorrectionStatus(self):
        status = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.correcting_label))).text
        assert status == constants.correcting_label
        add_documents_header = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.add_documents_header))).is_displayed()
        assert add_documents_header

    def replace_document(self, fileName):
        self.utils.getscreenshot("/4.Before_Document_Replace.png")
        self.click_file_menu()
        self.verifyOptionsUnderFileMenu()
        replace_document_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.replace_menu_item)))
        absolute_file_path_docx = os.path.abspath(fileName)
        replace_document_button.send_keys(absolute_file_path_docx)
        time.sleep(8)
        self.utils.getscreenshot("/5.After_Document_Replace.png")

    def clickPrimarySignButton(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.primary_sign_button))).click()

    def add_access_code(self, accesscode):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.recipient_menu))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.access_code))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.access_code_input))).send_keys(accesscode)