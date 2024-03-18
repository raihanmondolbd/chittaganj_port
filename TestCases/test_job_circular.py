import time
from TestCases.BaseTest import BaseTest
from Pages.dashboard_page import DashboardPage


class Test_JobCircular(BaseTest):
    def test_job_circular(self):
        db = DashboardPage(self.driver)
        db.click_on_first_details()
        db.click_on_eye_icon()
        db.click_on_apply_now_button()
        db.click_on_continue_without_login_button()
        db.enter_nid_number()
        db.upload_attachment()
        db.enter_date_of_birth()
        db.click_on_nid_verification()

    def test_form_fill_up(self):
        db = DashboardPage(self.driver)
        db.enter_father_name()
        db.enter_mother_name()
        otp = db.enter_mobile_number()
        db.enter_otp(otp)
        db.enter_email()
        db.select_religion()
        db.upload_photo()
        db.upload_signature()
        db.click_on_next_button()
        db.input_permanent_address()
        db.input_present_address()
        db.click_on_second_next_button()
        db.enter_hsc_information()
        db.enter_ssc_information()
        db.click_on_third_next_button()
        time.sleep(3)
