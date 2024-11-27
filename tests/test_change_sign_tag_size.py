from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.uploadPage import Upload_Page
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_Change_Sign_Tag_Size:

    def test_change_sign_size(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        utils = Util_Test(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        utils.create_directory(request.node.name)
        logger = Util_Test.initialize_logger('ChangeTagSize')
        utils.execute_script_with_banner("Started the Execution for changing the Signature Tag size")
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        try:
            Util_Test.write_custom_logs(logger, "Change signature Tag size script execution - Started")
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            utils.execute_script_with_banner("Home page is Displayed")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page")
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on start button to send Envelope")
            home.send_envelope()
            utils.execute_script_with_banner("Uploading the Document as a sender")
            upload.upload_envelope_documents(constants.envelope1_docx, False)
            Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
            utils.execute_script_with_banner("Adding first recipients and other details:")
            upload.clickSetSigningOrderCheckbox()
            Util_Test.write_custom_logs(logger, "Selected the set signing order checkbox")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
            utils.execute_script_with_banner("Adding second recipients and other details:")
            upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
            Util_Test.write_custom_logs(logger, "Added the recipient 2 details")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            add_sign = Add_Sign_Tags(driver)
            utils.execute_script_with_banner(logger, "Changing the size of Signature Tag")
            add_sign.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            utils.getscreenshot('/1.Before_changing_Signature_Tag_size_100%_resolution.png')
            add_sign.validateOptionsUnderSignature()
            Util_Test.write_custom_logs(logger, "Validated the options under the signature section")
            add_sign.change_sign_tag_size()
            Util_Test.write_custom_logs(logger, "Increased the signature tag size for recipient 1")
            utils.getscreenshot('/2.After_Changing_signature_Tag_size_200%_resolution.png')
            add_sign.select_signer(constants.index_two)
            Util_Test.write_custom_logs(logger, "Selected the Recipient2 from the drop down")
            add_sign.addSignatureTag(650)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2 ")
            add_sign.change_sign_tag_size()
            Util_Test.write_custom_logs(logger, "Increased the signature tag size for recipient 2.")
            Util_Test.write_custom_logs(logger,'Change signature Tag size script execution - completed')
        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            pytest.fail()
