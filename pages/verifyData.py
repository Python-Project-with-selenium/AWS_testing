from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from utilities.generateutils import generate_random_userName
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Util_Test
from testData import constants as constants
import time
import os


class Envelope_History:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Util_Test(driver)
        # Locators:
        self.manage_tab = "//button[@data-qa='header-MANAGE-tab-button']"
        self.sent_box = "button[data-qa='manage-sidebar-labels-sent-label']"
        self.select_document = "//div[contains(text(), 'document_name')]"
        self.open_document = "//a[@data-qa='page-thumbnail']"
        self.more_document = "button[data-qa='document-more']"
        self.envelope_action_history = "button[data-qa='envelope-action-history']"
        self.history_activity_row = "tr[data-qa='history-activity-row']"
        self.user_name_text = "(//td[contains(text(), 'Test Sender')])[1]"
        self.signature_id = "//td[contains(text(), '54cfffe6-35eb-4dd9-81e8-35ab08e0e62e')]"
        self.adopted_signature_id = "//td[contains(text(), '723bde61-2321-43f8-af2a-4d5a04843d65')]"
        self.close_button = "//button[@data-qa='history-modal-close']"
        self.reports_tab = "//button[@data-qa='header-REPORTS-tab-button']"
        self.envelope_button = "//button[@data-qa='Envelope']"
        self.view_button = "(//button[@data-qa='report-action'])[1]"
        self.date_range_DD = "button[data-qa='report-range-menu']"
        self.date_range_any = "button[data-qa='date_range_any']"
        self.custom_item = "//span[normalize-space()='Custom']"
        self.date_range_from_button = "button[data-qa='date-range-from-button']"
        self.day_picker = "(//div[@aria-selected='true'])[1]"
        self.present_day_checkbox = "//label[@data-qa='present-day-checkbox-label']"
        self.run_report = "//button[@data-qa='run-report']"
        self.report_result = "(//tr[@data-qa='report-result-row'])[1]"
        self.report_download = "//button[@data-qa='report-download-icon']"
        self.user_label = "//span[contains(text(), 'User')]"
        self.profile_icon = "//span[@data-qa='header-profile-menu-button-avatar']"
        self.my_preferences = "//button[@data-qa='header-choice-PREFERENCES-button']"
        self.regional_settings = "//button[@data-qa='regional-settings']"
        self.date_time_format = "//select[@data-qa='date-time-format-dropdown']"
        self.home_tab = "//span[@data-qa='header-HOME-tab-button-text']"
        self.action_required = "//button[@data-qa='action-required-count']"
        self.settings_tab = "//button[@data-qa='header-RADMIN-tab-button']"
        self.users_option = "//button[@data-qa='nav_link_authenticated.users']"
        self.add_user = "//button[@data-qa='users_add_user_btn']"
        self.user_email_text_box = "//label[contains(text(),'Email Address')]/../following-sibling::div//input"
        self.add_user_next_btn1 = "//button[@data-qa='add_user_step1_next_btn']"
        self.full_name_text_box = "//label[contains(text(),'Full Name')]/../following-sibling::div//input"
        self.add_user_next_btn2 = "//button[@data-qa='add_user_step2_next_btn']"
        self.access_code_text_box = "//label[contains(text(),'Access Code')]/../following-sibling::div//input"
        self.permission_profile_dropdown = "//select[@data-qa='add_user_ps_selector']"
        self.add_user_next_btn3 = "//button[@data-qa='add_user_step3_next_btn']"
        self.add_user_next_btn4 = "//button[@data-qa='add_user_step4_next_btn']"
        self.email_preferences = "//button[@data-qa='nav_link_authenticated.email-preferences']"
        self.users_list_page_title = "//h1[@data-qa='accountUserList_page_title']"
        self.email_preferences_checkbox1 = "(//label[@class='css-1n0yh7u'])[2]"
        self.email_preferences_checkbox2 = "(//label[@class='css-1n0yh7u'])[3]"
        self.save_button = "(//button[@data-qa='ds_ackbar_save_btn'])[1]"
        self.email_preferences_header = "//h1[@data-qa='email-preferences_page_title']"
        self.completed_files = "//button[@data-qa='completed-count']//span"
        self.start_button = "button[data-qa='manage-sidebar-actions-ndse-trigger']"
        self.receiving_select_all_checkbox = "//input[@data-qa='all-receiving-cb-value']"
        self.notification_select_all_checkbox = "//input[@data-qa='notification-all-cb-value']"
        self.cookies_alert = "//*[contains(text(), 'Accept Cookies')]"
        self.permission_dropdown = "//select[@data-qa='add_user_ps_selector']"
        self.cancel_button = "//button[@data-qa='ds_ackbar_cancel_btn']"
        self.user_name_search_box = "//input[@name='filter-input-box']"
        self.user_search_btn = "//button[@data-qa='filter-search-btn']"
        self.user_record = "//tr/td[@data-qa='Name_cell']/div"
        # Validating the options under users section
        self.add_user_option = "//span[contains(text(),'Add User')]"
        self.download_users_option = "//span[contains(text(),'Download Users')]"
        self.bulk_add_option = "//span[contains(text(),'Bulk Actions')]"
        self.bulk_update_option = "//span[contains(text(),'Bulk Update')]"
        # Validating the options under add user section
        self.enter_email_address_option = "//h2[contains(text(),'Enter Email Address')]"
        self.profile_information_option = "//h2[contains(text(),'Profile Information')]"
        self.security_option = "//h2[contains(text(),'Security')]"
        self.permission_profile_and_grouping_option = "//h2[contains(text(),'Permission Profile and Groups')]"
        # Validating the options under Email Preferences(EP)
        self.user_option_under_EP = "//span[normalize-space()='User']"
        self.api_user_under_EP = "//span[normalize-space()='API User']"
        # validating the option under user section and api user section
        self.for_signers_option = "//h2[contains(text(),'For Signers')]"
        self.for_sender_option = "//h2[contains(text(),'For Sender')]"
        self.dash_board_label = "//h4[contains(text(),'Dashboards')]"

        # Verify date format on signed Envelop

    def verify_dateFormat(self, fileName):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button))).is_displayed()
        # homeTab.click()
        completed_count = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.completed_files)))
        self.driver.execute_script("arguments[0].click();", completed_count)
        select_doc = self.select_document.replace("document_name", fileName)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, select_doc))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.open_document))).click()
        # time.sleep(10)
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                childWindow = handle
                self.driver.switch_to.window(childWindow)
        self.utils.getscreenshot("/date_format.png")
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(parentWindow)

    # Verify Envelope history
    def verify_envelope_history(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.more_document))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.envelope_action_history))).click()
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        label1 = self.driver.find_element(By.XPATH, self.user_label)
        scroll_origin = ScrollOrigin.from_element(label1)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 500).perform()
        self.utils.getscreenshot("/1.EnvelopeHistory.png")
        userLabel = self.driver.find_element(By.XPATH, self.user_label).text
        print(userLabel)
        text_userName = self.driver.find_element(By.XPATH, self.user_name_text).text
        print(text_userName)
        assert constants.sender_name in text_userName
        self.driver.find_element(By.XPATH, self.close_button).click()
        self.driver.switch_to.window(parentWindow)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.reports_tab))).click()
        dash_board_label = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.dash_board_label)))
        if dash_board_label:
            self.utils.getscreenshot("/2.Reports_page.png")
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, self.envelope_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.view_button))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.date_range_DD))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.custom_item))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.run_report))).click()
        report_result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.report_result))).text
        print(report_result)
        try:
            os.remove(constants.csv_envelope_report)
        except:
            print("downloads folder is empty")
        download = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.report_download)))
        self.driver.execute_script("arguments[0].click();", download)
        time.sleep(5)

    def creating_user(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.settings_tab))).click()
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
                By.XPATH, self.cookies_alert))).click()
        except:
            print("No Alert is displayed")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.users_option))).click()
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.add_user_option, self.download_users_option, self.bulk_add_option, self.bulk_update_option])

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user))).click()
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.enter_email_address_option, self.profile_information_option, self.security_option,
                    self.permission_profile_and_grouping_option])
        user_email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.user_email_text_box))).is_displayed()
        assert user_email
        self.utils.getscreenshot('/1.Add_user_page.png')
        random_user = generate_random_userName()
        user_name = random_user['full_name']

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.user_email_text_box))).send_keys(user_name + "@pharmateksol.com")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn1))).click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.XPATH, self.full_name_text_box))).send_keys(user_name)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn2))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.access_code_text_box))).send_keys(constants.access_code)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn3))).click()
        select = Select(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.permission_dropdown))))
        select.select_by_visible_text(constants.permission_profile_viewer)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_user_next_btn4))).click()
        users_list = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.users_list_page_title))).text
        assert users_list == constants.users_page_title
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name_search_box))).send_keys(user_name)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.user_search_btn))).click()
        self.utils.getscreenshot("/2.Added_user_details.png")
        username_in_record = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.user_record))).text
        print("username_in_record:", username_in_record)
        assert username_in_record == user_name

    def click_email_preferences(self):
        time.sleep(5)
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((By.XPATH, self.email_preferences))).click()
        self.utils.getscreenshot('/3.Options_under_email_preferences.png')

    def validatingOptionsUnderEmailPreferences(self):
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.user_option_under_EP, self.api_user_under_EP, self.for_sender_option, self.for_signers_option])

    def updating_email_preferences(self, screenshot=False):
        signer_selectAll_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.receiving_select_all_checkbox)))
        self.driver.execute_script("arguments[0].click();", signer_selectAll_checkbox)
        sender_selectAll_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.notification_select_all_checkbox)))
        self.driver.execute_script("arguments[0].click();", sender_selectAll_checkbox)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.save_button))).click()
        email_pref = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.XPATH, self.email_preferences_header))).text
        print(email_pref)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.XPATH, self.cancel_button))).is_displayed()
        time.sleep(2)
        if screenshot:
            self.utils.getscreenshot("/4.uncheck_email_preferences.png")

    def verifying_email_prefs_header(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.XPATH, self.email_preferences_header))).is_displayed()
