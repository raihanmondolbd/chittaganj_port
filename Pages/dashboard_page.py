import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Config.config import TestData
from Pages.BasePage import BasePage
from Locators.Locators import Locators


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super().__init__(driver)

    def click_on_first_details(self):
        self.click_element(self.locator.detailsFirst)

    def click_on_eye_icon(self):
        self.switch_to_new_tab()
        self.click_element(self.locator.viewIcon)

    def click_on_apply_now_button(self):
        self.click_element(self.locator.applyNowButton)

    def click_on_continue_without_login_button(self):
        self.click_element(self.locator.continueWithoutLogin)

    def enter_nid_number(self):
        self.enter_at(self.locator.nidTextField, TestData.NID_NUMBER)

    def upload_attachment(self):
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "images/nid.jpeg"))

        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(upload_file)

    def enter_date_of_birth(self):
        self.click_element(self.locator.dateOfBirth)
        month = self.get_element_text(self.locator.selectMonth)
        while month != "AUGUST 1995":
            self.click_element(self.locator.previusMonth)
            month = self.get_element_text(self.locator.selectMonth)
        self.click_element(self.locator.date_23)

    def click_on_nid_verification(self):
        self.click_element(self.locator.nidVerification)

    def enter_father_name(self):
        self.enter_at(self.locator.fatherName, TestData.FATHER_NAME)

    def enter_mother_name(self):
        self.enter_at(self.locator.motherName, TestData.MOTHER_NAME)

    def get_otp_from_alert(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        otp = alert_text[26:30]
        alert.accept()
        return otp

    def enter_mobile_number(self):
        self.enter_at(self.locator.mobileNumber, TestData.mobile_number(self))
        time.sleep(1)
        return self.get_otp_from_alert()

    def enter_otp(self, otp):
        try:
            self.enter_at(self.locator.otpNumber, otp)
            time.sleep(1)
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            print(e)

    def enter_email(self):
        self.enter_at(self.locator.email, TestData.EMAIL)

    def select_religion(self):
        select = Select(self.get_element(self.locator.religion))
        select.select_by_value("1")

    def upload_photo(self):
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "images/photo.jpeg"))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        file_input = self.driver.find_element(By.ID, self.locator.photo)
        file_input.send_keys(upload_file)

    def upload_signature(self):
        upload_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "images/signature.jpeg"))

        file_input = self.driver.find_element(By.ID, self.locator.signature)
        file_input.send_keys(upload_file)

    def click_on_next_button(self):
        self.click_element(self.locator.nextButton)

    def input_permanent_address(self):
        division = Select(self.get_element(self.locator.permanent_division))
        division.select_by_value("1")
        time.sleep(1)
        district = Select(self.get_element(self.locator.permanent_district))
        district.select_by_index("1")
        time.sleep(1)
        thana = Select(self.get_element(self.locator.permanent_thana))
        thana.select_by_value("10101")
        time.sleep(1)
        self.enter_at(self.locator.permanent_post_office_name, "Devgram")
        self.enter_at(self.locator.permanent_post_code, "2216")
        self.enter_at(self.locator.permanent_address, "Devgram")

    def input_present_address(self):
        division = Select(self.get_element(self.locator.present_division))
        division.select_by_visible_text("DHAKA")
        district = Select(self.get_element(self.locator.present_district))
        district.select_by_visible_text("DHAKA")
        thana = Select(self.get_element(self.locator.present_thana))
        thana.select_by_value("10101")
        self.enter_at(self.locator.present_post_office_name, "Dhaka G.P.O")
        self.enter_at(self.locator.present_post_code, "1000 ")
        self.enter_at(self.locator.present_address, "20/2, RUPNAGAR ABASHIK ELAKA, WARD NO-20(PART)")

    def click_on_second_next_button(self):
        self.click_element(self.locator.nextButton2)

    def enter_hsc_information(self):
        exam = Select(self.get_element(self.locator.education_0_exam))
        exam.select_by_visible_text("HSC")
        subject = Select(self.get_element(self.locator.education_0_subject))
        subject.select_by_visible_text("Science")
        exam_body = Select(self.get_element(self.locator.education_0_exam_body))
        exam_body.select_by_index("1")
        self.enter_at(self.locator.education_0_passing_year, "2016")
        result_type = Select(self.get_element(self.locator.education_0_result_type))
        result_type.select_by_index("1")
        self.enter_at(self.locator.education_0_result, "4")

    def enter_ssc_information(self):
        exam = Select(self.get_element(self.locator.education_1_exam))
        exam.select_by_visible_text("SSC")
        subject = Select(self.get_element(self.locator.education_1_subject))
        subject.select_by_visible_text("Science")
        exam_body = Select(self.get_element(self.locator.education_1_exam_body))
        exam_body.select_by_index("1")
        self.enter_at(self.locator.education_1_passing_year, "2014")
        result_type = Select(self.get_element(self.locator.education_1_result_type))
        result_type.select_by_index("1")
        self.enter_at(self.locator.education_1_result, "5")

    def click_on_third_next_button(self):
        self.click_element(self.locator.nextButton3)
